from google import genai
from openai import OpenAI
from dotenv import load_dotenv
import os

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
    messages
):

    # =====================================
    # GEMINI
    # =====================================

    if "gemini" in modelo.lower():

        system_instruction = ""

        historico = []

        for mensagem in messages:

            if mensagem["role"] == "system":

                system_instruction += (
                    mensagem["content"]
                    + "\n\n"
                )

            else:

                historico.append(
                    mensagem["content"]
                )

        response = (
            gemini_client.models.generate_content(

                model=modelo,

                config={
                    "system_instruction":
                    system_instruction
                },

                contents="\n\n".join(
                    historico
                )
            )
        )

        return response.text

    # =====================================
    # OPENAI
    # =====================================

    else:

        response = (
            openai_client.chat.completions.create(

                model=modelo,

                messages=messages
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )


# =========================================
# TESTE LOCAL
# =========================================

if __name__ == "__main__":

    messages = [

        {
            "role": "system",
            "content":
            "Você é um tutor socrático."
        },

        {
            "role": "user",
            "content":
            "O que é função do primeiro grau?"
        }
    ]

    resposta = gerar_resposta(

        "gpt-4o-mini",

        messages
    )

    print(
        "\n========== RESPOSTA ==========\n"
    )

    print(resposta)