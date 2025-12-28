from dotenv import load_dotenv
load_dotenv()

import os
import csv
import numpy as np
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------
# Load Embedder
# ---------------------------------------------------------
embedder = SentenceTransformer("BAAI/bge-small-en-v1.5")

# ---------------------------------------------------------
# Global psychiatric memory (shared across ALL patients)
# ---------------------------------------------------------
global_memory = []   # Each entry: {question, answer, embedding}

# ---------------------------------------------------------
# Per-patient history only (NOT memory)
# ---------------------------------------------------------
patient_profiles = {}  # patient_id → {history: ...}

# ---------------------------------------------------------
# Embedding helper
# ---------------------------------------------------------
def get_embedding(text: str):
    emb = embedder.encode(text)
    return emb.tolist()

# ---------------------------------------------------------
# Similarity function
# ---------------------------------------------------------
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

# ---------------------------------------------------------
# Load CSV (relative path)
# ---------------------------------------------------------
CSV_PATH = os.path.join(os.path.dirname(__file__), "patients_data.csv")

def load_csv():
    """Loads patient history + global psychiatric memories."""
    global global_memory, patient_profiles

    if not os.path.exists(CSV_PATH):
        print(f"⚠️ CSV not found at: {CSV_PATH}")
        return

    print(f"📄 Loading patient memory from: {CSV_PATH}")

    try:
        with open(CSV_PATH, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                pid = row["patient_id"]

                # Store patient history separately
                if pid not in patient_profiles:
                    patient_profiles[pid] = {
                        "history": row.get("history", "General mental health background")
                    }

                # Encode question to embedding
                emb = get_embedding(row["question"])

                # Store in global memory (shared)
                global_memory.append({
                    "patient_id": pid,
                    "question": row["question"],
                    "answer": row["answer"],
                    "embedding": emb
                })

        print("✅ CSV loaded successfully.")

    except Exception as e:
        print("❌ ERROR reading CSV:", e)

# ---------------------------------------------------------
# Run CSV load immediately
# ---------------------------------------------------------
load_csv()

# ---------------------------------------------------------
# Search global memory
# ---------------------------------------------------------
def find_similar_question(new_question):
    """
    Searches ONLY global_memory.
    Returns: best_score, best_answer
    """
    new_emb = get_embedding(new_question)
    best_score = -1
    best_answer = None

    for item in global_memory:
        score = cosine_similarity(new_emb, item["embedding"])
        if score > best_score:
            best_score = score
            best_answer = item["answer"]

    return best_score, best_answer






