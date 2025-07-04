from app.schemas.schedules_schema import ScheduleRequest

def build_prompt(data: ScheduleRequest) -> str:
    return f"""
Genera un horario de clases a partir del siguiente historial académico y preferencias del estudiante.

Historial de materias cursadas: {', '.join(data.record)}

Preferencias del estudiante:
- Horario preferido: {data.preferences["hour"]}
- Días preferidos: {data.preferences["days"]}

Cursos disponibles para simular:
{chr(10).join([f"- {c.name} ({c.code}) con grupos: {', '.join(c.groups)}" for c in data.curses_simulated or []])}

Entrega la respuesta en formato JSON, con este esquema:

{{
  "schedule": [
    {{
      "course": "INF201",
      "group": "group A",
      "day": "Monday",
      "hour": "08:00"
    }}
  ]
}}

No incluyas explicaciones, solo el JSON.
"""
