import requests
from app.core.config import OLLAMA_URL

async def ask_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": "gemma:2b",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        return data.get("message", {}).get("content", "⚠️ No se recibió respuesta válida del modelo.")
    except requests.exceptions.RequestException as e:
        return f"[ERROR CONEXIÓN IA]: {e}"
