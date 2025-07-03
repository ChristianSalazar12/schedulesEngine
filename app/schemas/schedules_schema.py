from pydantic import BaseModel
from typing import List,Optional,Dict

class CursoSimulado(BaseModel):
    code:str
    name:str
    groups:List[str]

class ScheduleRequest(BaseModel):
    record: List[str]
    preferences: Dict[str,str]
    curses_simulated: Optional[List[CursoSimulado]]