# analise.py

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# =========================================
# PATHS
# =========================================

BASE_DIR = Path(__file__).parents[1]

DADOS_DIR = BASE_DIR / "dados"

CSV_PERFIS = DADOS_DIR / "perfis.csv"
CSV_CONVERSAS = DADOS_DIR / "conversas.csv"
CSV_FEEDBACK = DADOS_DIR / "feedback.csv"

RELATORIO = BASE_DIR / "relatorio.md"


# =========================================
# CARREGAR DADOS
# =========================================

def carregar_dados():

    perfis = pd.read_csv(CSV_PERFIS)
    conversas = pd.read_csv(CSV_CONVERSAS)
    feedbacks = pd.read_csv(CSV_FEEDBACK)

    return perfis, conversas, feedbacks


# =========================================
# LIMPEZA
# =========================================

def limpar_dados(df):

    return df.drop_duplicates()


# =========================================
# GERAR ÍNDICES
# =========================================

def gerar_indices(df):

    df["indice_reflexao"] = (
        df["nota_reflexao"] +
        df["nota_pensamento"] +
        df["nota_autonomia"]
    ) / 3

    df["indice_contextualizacao"] = (
        df["nota_contexto"] +
        df["nota_cotidiano"]
    ) / 2

    df["indice_engajamento"] = (
        df["nota_engajamento"] +
        df["nota_interesse"]
    ) / 2

    df["indice_sobrecarga"] = (
        df["nota_dificuldade"] +
        df["nota_frustracao"]
    ) / 2
    #o índice IDA é um índice próprio cirado para mensurar a coerência do propósito do TCC
    #com base nos anteriores
    df["IDA"] = (
        df["indice_reflexao"] * 0.4 +
        df["indice_contextualizacao"] * 0.3 +
        df["indice_engajamento"] * 0.3
    )#mais peso à reflexão

    return df


# =========================================
# ESTATÍSTICAS
# =========================================

def estatisticas(df):

    stats = {}

    colunas = [
        "indice_reflexao",
        "indice_contextualizacao",
        "indice_engajamento",
        "indice_sobrecarga",
        "IDA"
    ]

    for coluna in colunas:

        stats[coluna] = {
            "media": round(df[coluna].mean(), 2),
            "desvio": round(df[coluna].std(), 2)
        }

    return stats


# =========================================
# COMPARAÇÃO ENTRE MODOS
# =========================================

def comparar_modos(df):

    return df.groupby("modo")[
        [
            "indice_reflexao",
            "indice_contextualizacao",
            "indice_engajamento",
            "indice_sobrecarga",
            "IDA"
        ]
    ].mean().round(2)


# =========================================
# COMPARAÇÃO ENTRE MODELOS
# =========================================

def comparar_modelos(df):

    return df.groupby("modelo")[
        [
            "indice_reflexao",
            "indice_contextualizacao",
            "indice_engajamento",
            "indice_sobrecarga",
            "IDA"
        ]
    ].mean().round(2)


# =========================================
# PROFUNDIDADE
# =========================================

def analisar_profundidade(df):

    return df.groupby("profundidade")[
        [
            "indice_reflexao",
            "indice_sobrecarga",
            "IDA"
        ]
    ].mean().round(2)


# =========================================
# PERFIS
# =========================================

def analisar_perfis(perfis, feedbacks):

    df = pd.merge(
        perfis,
        feedbacks,
        on="session_id"
    )

    cursos = df.groupby("curso")["IDA"].mean().round(2)

    dificuldade = df.groupby(
        "dificuldade"
    )["IDA"].mean().round(2)

    emocional = df.groupby(
        "emocional"
    )["IDA"].mean().round(2)

    return cursos, dificuldade, emocional


# =========================================
# PALAVRAS FREQUENTES
# =========================================

def palavras_frequentes(df):

    texto = ""

    colunas = [
        "aprendizado",
        "experiencia",
        "sugestoes"
    ]

    for coluna in colunas:

        texto += " ".join(
            df[coluna]
            .fillna("")
            .astype(str)
        )

    palavras = texto.lower().split()

    stopwords = [
        "para",
        "mais",
        "muito",
        "sobre",
        "porque",
        "essa",
        "isso",
        "com",
        "uma",
        "foi"
    ]

    frequencia = {}

    for palavra in palavras:

        palavra = palavra.strip(".,!?;:")

        if len(palavra) > 4 and palavra not in stopwords:

            frequencia[palavra] = (
                frequencia.get(palavra, 0) + 1
            )

    ordenado = sorted(
        frequencia.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ordenado[:20]


# =========================================
# CONVERSAS
# =========================================

def analisar_conversas(conversas):

    total = len(conversas)

    media_pergunta = (
        conversas["pergunta"]
        .astype(str)
        .str.len()
        .mean()
    )

    media_resposta = (
        conversas["resposta"]
        .astype(str)
        .str.len()
        .mean()
    )

    return {
        "total": total,
        "media_pergunta": round(media_pergunta, 2),
        "media_resposta": round(media_resposta, 2)
    }


# =========================================
# CORRELAÇÕES
# =========================================

def correlacoes(df):

    colunas = [
        "profundidade",
        "indice_reflexao",
        "indice_contextualizacao",
        "indice_engajamento",
        "indice_sobrecarga",
        "IDA"
    ]

    return df[colunas].corr().round(2)


# =========================================
# GRÁFICOS
# =========================================

def gerar_graficos(df):

    pasta = BASE_DIR / "graficos"

    pasta.mkdir(exist_ok=True)

    # IDA por modo

    medias = df.groupby("modo")["IDA"].mean()

    medias.plot(kind="bar")

    plt.title("IDA por modo pedagógico")

    plt.ylabel("Média")

    plt.savefig(
        pasta / "ida_modo.png",
        bbox_inches="tight"
    )

    plt.close()

    # Reflexão por modelo

    medias = df.groupby(
        "modelo"
    )["indice_reflexao"].mean()

    medias.plot(kind="bar")

    plt.title("Reflexão por modelo")

    plt.ylabel("Média")

    plt.savefig(
        pasta / "reflexao_modelo.png",
        bbox_inches="tight"
    )

    plt.close()


# =========================================
# RELATÓRIO
# =========================================

def gerar_relatorio(
    stats,
    modos,
    modelos,
    profundidade,
    cursos,
    dificuldade,
    emocional,
    palavras,
    conversa_stats,
    correlacao
):

    texto = f"""
# Relatório de Análise Pedagógica

## Estatísticas Gerais

### Índice de Reflexão

- Média: {stats["indice_reflexao"]["media"]}
- Desvio padrão: {stats["indice_reflexao"]["desvio"]}

### Índice de Contextualização

- Média: {stats["indice_contextualizacao"]["media"]}
- Desvio padrão: {stats["indice_contextualizacao"]["desvio"]}

### Índice de Engajamento

- Média: {stats["indice_engajamento"]["media"]}
- Desvio padrão: {stats["indice_engajamento"]["desvio"]}

### IDA

- Média: {stats["IDA"]["media"]}
- Desvio padrão: {stats["IDA"]["desvio"]}

---

## Comparação entre modos pedagógicos

{modos.to_markdown()}

---

## Comparação entre modelos

{modelos.to_markdown()}

---

## Influência da profundidade

{profundidade.to_markdown()}

---

## Cursos

{cursos.to_markdown()}

---

## Dificuldade declarada

{dificuldade.to_markdown()}

---

## Estado emocional

{emocional.to_markdown()}

---

## Conversas

- Total de interações: {conversa_stats["total"]}
- Média de caracteres das perguntas:
{conversa_stats["media_pergunta"]}
- Média de caracteres das respostas:
{conversa_stats["media_resposta"]}

---

## Palavras mais frequentes

"""

    for palavra, freq in palavras:

        texto += f"- {palavra}: {freq}\n"

    texto += f"""

---

## Correlações

{correlacao.to_markdown()}

---

## Considerações preliminares

Os resultados indicam tendências importantes
relacionadas à aprendizagem dialógica,
reflexão crítica, contextualização e
engajamento dos estudantes.

A análise sugere que diferentes modos
pedagógicos e níveis de profundidade
impactam diretamente a experiência
educacional proporcionada pela IA.

"""

    with open(
        RELATORIO,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(texto)


# =========================================
# MAIN
# =========================================

if __name__ == "__main__":

    perfis, conversas, feedbacks = carregar_dados()

    perfis = limpar_dados(perfis)
    conversas = limpar_dados(conversas)
    feedbacks = limpar_dados(feedbacks)

    feedbacks = gerar_indices(feedbacks)

    stats = estatisticas(feedbacks)

    modos = comparar_modos(feedbacks)

    modelos = comparar_modelos(feedbacks)

    profundidade = analisar_profundidade(feedbacks)

    cursos, dificuldade, emocional = analisar_perfis(
        perfis,
        feedbacks
    )

    palavras = palavras_frequentes(feedbacks)

    conversa_stats = analisar_conversas(conversas)

    correlacao = correlacoes(feedbacks)

    gerar_graficos(feedbacks)

    gerar_relatorio(
        stats,
        modos,
        modelos,
        profundidade,
        cursos,
        dificuldade,
        emocional,
        palavras,
        conversa_stats,
        correlacao
    )

    print("\nRelatório gerado com sucesso.\n")