from app.services.llm_local_ia import ask_ollama
from app.schemas.schedules_schema import ScheduleRequest
from app.services.prompt_builder import build_prompt  # si lo separas en otro archivo

async def generate_schedule(data: ScheduleRequest) -> dict:
    prompt = build_prompt(data)
    try:
        response = await ask_ollama(prompt)
        return {"respuesta": response}
    except Exception as e:
        return {"respuesta": f"[ERROR GENERANDO HORARIO]: {e}"}
