import openai
from app.core.config import OPENAI_API_KEY,OPENAI_MODEL 
 

async def ask_openai(prompt: str) -> str:
    openai.api_key = OPENAI_API_KEY

    response= openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content