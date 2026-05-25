from pathlib import Path


# =========================================
# CARREGAR PROMPT BASE
# =========================================

def carregar_prompt(modo):

    arquivo = (
        Path(__file__).parents[1]
        / "prompts"
        / f"{modo}.txt"
    )

    with open(
        arquivo,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


# =========================================
# MONTAR CONTEXTO DO ALUNO
# =========================================

def montar_prompt(
    perfil,
    pergunta,
    profundidade
):

    profundidade_contexto = {
        1: "O estudante prefere respostas mais diretas.",
        2: "O estudante aceita pequenas reflexões.",
        3: "O estudante prefere equilíbrio entre explicação e questionamento.",
        4: "O estudante prefere perguntas guiadas e reflexão.",
        5: "O estudante deseja forte condução maiêutica."
    }

    contexto = f"""
# PERFIL DO ESTUDANTE

Nome:
{perfil.get('nome', '')}

Idade:
{perfil.get('idade', '')}

Curso/Série:
{perfil.get('curso', '')}

Tema:
{perfil.get('tema', '')}

Interesses:
{perfil.get('hobbies', '')}

Objetivo:
{perfil.get('objetivo', '')}

Maior dificuldade:
{perfil.get('maior_dificuldade', '')}

Forma preferida de aprendizagem:
{perfil.get('aprende_melhor', '')}

Estado emocional:
{perfil.get('emocional', '')}

# PROFUNDIDADE REFLEXIVA

Nível:
{profundidade}/5

Descrição:
{profundidade_contexto.get(profundidade)}

# INSTRUÇÕES IMPORTANTES

- Use exemplos contextualizados.
- Relacione explicações aos interesses do estudante.
- Adapte a linguagem à idade e dificuldade.
- Priorize perguntas reflexivas antes da resposta final.
- Evite entregar respostas prontas imediatamente.

# PERGUNTA DO ESTUDANTE

{pergunta}
"""

    return contexto


if __name__ == "__main__":

    perfil_teste = {
        "nome": "João",
        "tema": "Função do 1º grau",
        "hobbies": "Futebol, Jogos",
        "objetivo": "Vestibular"
    }

    system_prompt = carregar_prompt(
        "socratico"
    )

    user_prompt = montar_prompt(
        perfil_teste,
        "Como funciona função do primeiro grau?",
        4
    )

    print("\n========== SYSTEM ==========\n")
    print(system_prompt)

    print("\n========== USER ==========\n")
    print(user_prompt)