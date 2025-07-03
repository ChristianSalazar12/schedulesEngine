from app.core.llm_provider import ask_llm

async def generate_schedule(data):
    prompt = f"Genera un horario para: {data.model_dump()}"
    return {"respuesta": await ask_llm(prompt)}