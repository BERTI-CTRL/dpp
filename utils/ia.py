from google import genai
from openai import OpenAI
from dotenv import load_dotenv
import os
from utils.prompts import carregar_prompt,montar_prompt

load_dotenv()

# =========================================
# CLIENTES
# =========================================

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# =========================================
# GERAR RESPOSTA
# =========================================

def gerar_resposta(
    modelo,
    system_prompt,
    user_prompt
):

    # =====================================
    # GEMINI
    # =====================================

    if "gemini" in modelo.lower():

        response = gemini_client.models.generate_content(

            model=modelo,

            config={
                "system_instruction": system_prompt
            },

            contents=user_prompt
        )

        return response.text

    # =====================================
    # OPENAI
    # =====================================

    else:

        response = openai_client.chat.completions.create(

            model=modelo,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response.choices[0].message.content
    

# TESTE LOCAL
# =========================================

if __name__ == "__main__":

    system_prompt = """
Você é um tutor socrático.
"""

    user_prompt = """
Aluno gosta de futebol.

Pergunta:
O que é função do primeiro grau?
"""

    resposta = gerar_resposta(
        "gemini-2.5-flash",
        system_prompt,
        user_prompt
    )

    print("\n========== RESPOSTA ==========\n")

    print(resposta)