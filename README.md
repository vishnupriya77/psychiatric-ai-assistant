🧠 Psychiatric AI Assistant (RAG-Based POC)

A lightweight Retrieval-Augmented Generation (RAG) system designed for psychiatric support and mental-health research.
The assistant personalizes responses using patient-specific memory, semantic search, and OpenRouter LLMs.

🚀 Key Features

RAG Pipeline → Retrieves similar past questions using BGE embeddings (bge-small-en-v1.5)
Multi-Patient Memory → Each patient has their own history & Q/A records
LLM Fallback → If no similar question is found, system calls OpenRouter (free models)
Auto-Learning → New Q/A pairs are embedded and stored for future retrieval
Frontend Chat UI → Simple WhatsApp-style interface for real usage

🧪 How It Works (RAG Flow)

User asks a question
System generates embedding → performs semantic search
If similarity ≥ 0.97 → return stored memory
Else → call LLM with patient history
New answer is stored + embedded for next time
