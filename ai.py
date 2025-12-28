from dotenv import load_dotenv
load_dotenv()

import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
def generate_answer(history, question):
    q = question.lower().strip()

    # Friendly greeting responses
    if q in ["hi", "hello", "hey", "hi there", "hola"]:
        return "Hi there, I'm here to listen. How are you feeling today?"

    # Neutral check for “how are you”
    if "how are you" in q:
        return "I'm here to support you. How have you been feeling emotionally lately?"

def generate_answer(history, question):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",   
        "X-Title": "Psychiatric-AI-POC",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [
            {"role": "system", "content": "You are a safe, empathetic mental health assistant. Do not diagnose or give medical advice."},
            {"role": "user", "content": f"Patient History:\n{history}\n\nQuestion:\n{question}"}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        res = response.json()
    except Exception:
        return "Error: Invalid JSON response from OpenRouter"

    print("OPENROUTER RAW RESPONSE:", res)

    if "error" in res:
        return f"Error from OpenRouter: {res['error']}"

    if "choices" not in res:
        return f"OpenRouter did not return 'choices': {res}"

    return res["choices"][0]["message"]["content"]



