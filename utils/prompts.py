from pathlib import Path

def carregar_prompt(modo):

    arquivo = Path("prompts") / f"{modo}.txt"

    with open(arquivo, "r", encoding="utf-8") as f:
        return f.read()
    
def montar_prompt(
    prompt_base,
    perfil,
    pergunta,
    profundidade
):

    contexto = f"""
Aluno:
- Nome: {perfil['nome']}
- Idade: {perfil['idade']}
- Interesses: {perfil['hobbies']}
- Tema: {perfil['tema']}

A profundidade indica o quanto o aluno quer a resposta imediata e o quanto ele quer refletir.
Indo de 1 a 5, onde 5 é o mais maiêutico, a profundidade para o aluno {perfil['nome']} é {profundidade}.

Pergunta do aluno:
{pergunta}
"""

    return prompt_base + "\n" + contexto