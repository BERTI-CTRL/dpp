from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
def gerar_resposta(prompt):
    client = genai.Client()

    response = client.models.generate_content(
        model= 'gemini-3.1-flash-lite',
        config={
            "system_instruction":{prompt}
        }
    )