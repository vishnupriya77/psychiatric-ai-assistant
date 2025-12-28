🧠 Psychiatric AI Assistant (RAG-Based Mental Health Support System)

This project is a Retrieval-Augmented Generation (RAG) powered psychiatric assistant designed to simulate how clinicians can store patient history, recall past interactions, and generate safe, contextual responses.
It combines semantic search, LLM reasoning, and patient-specific memory into a simple but powerful mental-health AI prototype.

🌟 Features
🔹 1. RAG Memory System (Semantic Search)

Uses BGE-small (bge-small-en-v1.5) embeddings to convert questions into vectors.

Performs cosine similarity search to find previously asked questions.

If similarity score ≥ 0.97 → returns the stored answer instantly.

🔹 2. LLM Fallback (OpenRouter)

When a question is new, the assistant:

Reads the patient’s mental health history,

Sends the query + history to an OpenRouter LLM (e.g., Llama / Mistral),

Returns a tailored and safe response.

🔹 3. Auto-Learning Memory

Every new Q/A pair is:

Embedded,

Stored in memory,

Used for future retrieval.

This creates a growing personalized psychiatric knowledge base.

🔹 4. Multi-Patient Support

Each patient has:

A unique ID

A history

Separate Q/A memory

System responds differently depending on the patient’s context.

🔹 5. Minimalist Frontend (Chat UI)

WhatsApp-style clean chat interface

Sends questions to FastAPI backend

Displays LLM or memory-based responses

🚀 How the System Works

User asks a question

System embeds the question → searches memory using cosine similarity

If similar question found → return memory answer

If not:

Retrieve patient history

Send query to OpenRouter LLM

Return AI-generated answer

Store new answer in memory for future use

This pipeline allows:

Faster responses

High consistency

Patient-aware personalization

Cost-efficient LLM usage

🙌 Contributions & Extensions

You can extend this POC to include:

Vector database (Pinecone / Chroma)

Crisis detection (self-harm classifier)

Fine-tuned patient-specific LLMs

Secure authentication & role-based access

EMR (Electronic Medical Record) integration
