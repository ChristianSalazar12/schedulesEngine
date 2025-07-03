# from app.services.llm_local_ia import ask_openai
from app.services.llm_local_ia import ask_ollama
from app.core.config import LLM_PROVIDER

async def ask_llm(prompt:str) -> str:
    # if LLM_PROVIDER.upper()== "OPENAI":
    #     return await ask_openai(prompt)
    return await ask_ollama(prompt)