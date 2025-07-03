from fastapi import APIRouter
from app.services.schedules_service import generate_schedule
from app.schemas.schedules_schema import ScheduleRequest

router = APIRouter()

@router.post("/generate-schedule")
async def generate(data:ScheduleRequest):
    return await generate_schedule(data)