from fastapi import FastAPI
from models import QuestionRequest
from memory import find_similar_question, get_embedding, global_memory, patient_profiles
from ai import generate_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
def ask(payload: QuestionRequest):
    patient_id = payload.patient_id
    question = payload.question

    # -------------------------------
    # 1. Find similar question (global memory)
    # -------------------------------
    score, stored_answer = find_similar_question(question)

    if score > 0.90:   # Good threshold
        return {
            "source": "memory",
            "similarity_score": score,
            "answer": stored_answer
        }

    # -------------------------------
    # 2. No match → generate AI answer
    # -------------------------------
    history = patient_profiles.get(patient_id, {}).get("history", "")
    ai_answer = generate_answer(history, question)

    # -------------------------------
    # 3. Store LLM answer into GLOBAL MEMORY
    # -------------------------------
    embedding = get_embedding(question)

    global_memory.append({
        "patient_id": patient_id,
        "question": question,
        "answer": ai_answer,
        "embedding": embedding
    })

    return {
        "source": "ai",
        "similarity_score": score,
        "answer": ai_answer
    }

@app.get("/")
def root():
    return {"message": "Psychiatric AI POC running with OpenRouter + global memory!"}



