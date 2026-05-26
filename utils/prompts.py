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
# PERFIL DO ALUNO
# =========================================

def montar_contexto_perfil(
    perfil
):

    return f"""
PERFIL DO ESTUDANTE

Nome:
{perfil.get("nome", "")}

Idade:
{perfil.get("idade", "")}

Curso:
{perfil.get("curso", "")}

Tema:
{perfil.get("tema", "")}

Objetivo:
{perfil.get("objetivo", "")}

Interesses:
{perfil.get("hobbies", "")}

Maior dificuldade:
{perfil.get("maior_dificuldade", "")}

Forma de aprendizagem:
{perfil.get("aprende_melhor", "")}

Estado emocional:
{perfil.get("emocional", "")}

Preferência de resposta:
{perfil.get("estilo_resposta", "")}
"""
    

# =========================================
# MEMÓRIA PEDAGÓGICA
# =========================================

def montar_memoria(
    memoria
):

    return f"""
MEMÓRIA PEDAGÓGICA

Conceitos compreendidos:

{memoria["conceitos_compreendidos"]}

Conceitos com dificuldade:

{memoria["conceitos_dificuldade"]}

Hipóteses levantadas pelo aluno:

{memoria["hipoteses"]}
"""