from fastapi import FastAPI
from app.api.routes_schedules import router as schedule_router

app = FastAPI()

app.include_router(schedule_router)  # no uses prefix aquí
