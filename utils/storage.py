# storage.py

from datetime import datetime
import streamlit as st
import pandas as pd
import gspread
from pathlib import Path

from oauth2client.service_account import (
    ServiceAccountCredentials
)


# =========================================
# CONFIG
# =========================================

NOME_PLANILHA = "IA_Educacional"

ARQUIVO_CREDENCIAIS = "credenciais.json"


# =========================================
# AUTENTICAÇÃO
# =========================================
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
] 
if Path("credenciais.json").exists():

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credenciais.json",
        scope
    )

else:

    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        st.secrets["gcp_service_account"],
        scope
    )

client = gspread.authorize(creds)

planilha = client.open(NOME_PLANILHA)


# =========================================
# ABAS
# =========================================

aba_perfis = planilha.worksheet("perfis")

aba_conversas = planilha.worksheet("conversas")

aba_feedback = planilha.worksheet("feedback")


# =========================================
# SALVAR PERFIL
# =========================================

def salvar_perfil(
    session_id,
    nome,
    idade,
    curso,
    hobbies,
    dificuldade,
    tema,
    objetivo,
    tempo_estudo,
    maior_dificuldade,
    aprende_melhor,
    emocional,
    estilo_resposta
):

    aba_perfis.append_row([

        session_id,


        str(datetime.now()),

        nome,

        idade,

        curso,

        ", ".join(hobbies),

        dificuldade,

        tema,

        objetivo,

        tempo_estudo,

        maior_dificuldade,

        ", ".join(aprende_melhor),

        emocional,

        estilo_resposta

    ])


# =========================================
# SALVAR CONVERSA
# =========================================

def salvar_conversa(

    session_id,

    numero_interacao, #para suportar as várias interações dentro de uma mesma sessão

    nome,

    pergunta,

    resposta,

    modelo,

    modo,

    profundidade
):

    aba_conversas.append_row([

        session_id,

        numero_interacao,

        str(datetime.now()),

        nome,

        pergunta,

        resposta,

        modelo,

        modo,

        profundidade

    ])

# =========================================
# SALVAR FEEDBACK
# =========================================

def salvar_feedback(

    session_id,

    modelo,

    modo,

    profundidade,

    nota_reflexao,

    nota_pensamento,

    nota_autonomia,

    nota_contexto,

    nota_cotidiano,

    nota_engajamento,

    nota_interesse,

    nota_dificuldade,

    nota_frustracao,

    comparacao,

    aprendizado,

    experiencia,

    sugestoes
):

    aba_feedback.append_row([

        session_id,

        str(datetime.now()),

        modelo,

        modo,

        profundidade,

        nota_reflexao,

        nota_pensamento,

        nota_autonomia,

        nota_contexto,

        nota_cotidiano,

        nota_engajamento,

        nota_interesse,

        nota_dificuldade,

        nota_frustracao,

        comparacao,

        aprendizado,

        experiencia,

        sugestoes

    ])


# =========================================
# CARREGAR PERFIS
# =========================================

def carregar_perfis():

    dados = aba_perfis.get_all_records()

    return pd.DataFrame(dados)


# =========================================
# CARREGAR CONVERSAS
# =========================================

def carregar_conversas():

    dados = aba_conversas.get_all_records()

    return pd.DataFrame(dados)


# =========================================
# CARREGAR FEEDBACK
# =========================================

def carregar_feedback():

    dados = aba_feedback.get_all_records()

    return pd.DataFrame(dados)

def buscar_perfis_aluno(nome_aluno, idade):

    df = carregar_perfis()

    df.columns = df.columns.str.strip()

    nome_aluno = nome_aluno.strip().upper()

    

    df_filtrado = df[
        (
            df["nome"]
            .astype(str)
            .str.strip()
            .str.upper()
            == nome_aluno
        )
        &
        (
            df["idade"] == idade
        )
    ]

    st.write("FILTRADO")
    st.write(df_filtrado)

    if df_filtrado.empty:
        return None

    return df_filtrado.iloc[-1].to_dict()


if __name__ == "__main__":
    # Exemplo de uso
    perfis = carregar_perfis()
    print(type(perfis))

    print(perfis.columns)