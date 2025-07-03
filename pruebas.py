from app.schemas.schedules_schema import ScheduleRequest

data = {
    "record": ["INF101", "MAT102"],
    "preferences": {
        "hour": "morning",
        "days": "Monday to Friday"
    },
    "curses_simulated": [
        {
            "code": "INF201",
            "name": "Algorithms",
            "groups": ["group A", "group B"]
        }
    ]
}

req = ScheduleRequest(**data)
print(req)
