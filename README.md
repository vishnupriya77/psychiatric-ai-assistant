🧠 Psychiatric AI Assistant (RAG-Based Mental Health Support)

A Retrieval-Augmented Generation (RAG) system that simulates how psychiatric tools store patient history, retrieve past interactions, and generate safe, personalized mental-health responses. The system combines semantic search (embeddings) + LLM reasoning + patient-specific memory, wrapped in a clean FastAPI backend with a simple chat UI.

🌟 Key Features

🔹 1. RAG Memory Search (Semantic Retrieval)

Uses BGE-small-en-v1.5 embeddings

Converts all questions into vectors

Performs cosine similarity search

If similarity ≥ 0.97 → returns stored answer

Gives consistent behaviour across sessions

🔹 2. LLM Fallback for New Questions

When no similar question exists:

Loads patient history

Sends structured prompt to OpenRouter (Llama/Mistral etc.)

Generates a safe, contextual psychiatric response

This ensures personalized, clinically-aware answers.

🔹 3. Auto-Learning Memory

Every new question/answer pair is:

Embedded

Saved under the patient’s ID

Used for future RAG retrieval

The system gets smarter with every conversation.

🔹 4. Multi-Patient Support

Each patient has:

Unique ID

Psychiatric history

Individual memory store (Q/A + embeddings)

You can load 1…N patients via a CSV file.

🔹 5. Clean WhatsApp-Style Chat UI

Frontend features:

Bubble chat

Typing indicator

Sends patient_id + question

Shows memory-based or LLM-generated answers

🏗️ Architecture Overview

Frontend (HTML Chat UI)
           │
           ▼
FastAPI Backend → RAG Memory → (if match) Return Answer
           │
           └──→ LLM (OpenRouter) → Save to Memory → Return Answer

🧪 Example Interaction Flow

User asks: “Why do I feel anxious at night?”

System embeds question & searches memory

If similar Q exists → returns stored answer

If not:

Loads patient history

Passes everything to LLM

Generates response

Saves it for future queries

This mirrors real-world digital mental-health assistants.
