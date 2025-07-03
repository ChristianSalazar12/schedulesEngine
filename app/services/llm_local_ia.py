import requests
from app.core.config import OLLAMA_URL


async def ask_ollama(prompt: str) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False},
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    return data.get("response", "Error en la respuesta de Ollama")
