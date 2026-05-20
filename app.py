# Interface Streamlit — TCC IA Socrática


import streamlit as st
"""from utils.ia import gerar_resposta
from utils.storage import (
    salvar_perfil,
    salvar_conversa,
    salvar_feedback
)

from utils.prompts import carregar_prompt"""



# =========================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================

st.set_page_config( 
    page_title="Tutor Socrático IA",
    page_icon="🧠",
    layout="wide"
)

# =========================================
# ESTILO VISUAL
# =========================================

st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
    }

    h1, h2, h3 {
        color: white;
    }

    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {
        color: white !important;
        font-weight: bold;
    }

    .stButton button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-size: 16px;
        font-weight: bold;
    }

    .perfil-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    .chat-box {
        background-color: #111827;
        padding: 20px;
        border-radius: 15px;
    }

    .feedback-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================
# TÍTULO PRINCIPAL
# =========================================

st.title("🧠 Tutor Socrático com IA")
st.markdown(
    """
    Sistema baseado em perguntas reflexivas inspirado em:

    - Maiêutica Socrática
    - Paulo Freire
    - Aprendizagem contextualizada
    """
)

# =========================================
# ABAS PRINCIPAIS
# =========================================

aba1, aba2, aba3 = st.tabs([
    "👤 Perfil do Aluno",
    "💬 Chat IA",
    "📊 Feedback"
])

# =========================================
# ABA 1 — PERFIL
# =========================================

with aba1:

    st.markdown('<div class="perfil-box">', unsafe_allow_html=True)

    st.header("👤 Perfil do Estudante")

    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=10, max_value=100)
        curso = st.text_input("Curso / Série")

    with col2:
        hobbies = st.multiselect(
            "Interesses / Hobbies",
            [
                "Música",
                "Futebol",
                "Academia",
                "Jogos",
                "Arte",
                "Programação",
                "Filmes",
                "Leitura",
                'Filosofia',
                'Robótica',
                'Psicologia'
            ]
        )

        dificuldade = st.selectbox(
            "Nível de dificuldade",
            [
                "Iniciante",
                "Intermediário",
                "Avançado"
            ]
        )

        tema = st.text_input("Tema que deseja estudar")

    st.button("Salvar Perfil")

    st.markdown('</div>', unsafe_allow_html=True)










# =========================================
# ABA 2 — CHAT IA
# =========================================

with aba2:

    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    st.header("💬 Conversa com a IA")

    # Histórico do chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensagens antigas
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada do usuário
    prompt = st.chat_input("Digite sua pergunta...")

    if prompt:

        # Mensagem do usuário
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        # RESPOSTA SIMULADA
        resposta_ia = "Interessante... antes de responder diretamente, me diga: como você relacionaria isso ao seu cotidiano?"

        st.session_state.messages.append({
            "role": "assistant",
            "content": resposta_ia
        })

        with st.chat_message("assistant"):
            st.markdown(resposta_ia)

    st.markdown('</div>', unsafe_allow_html=True)



















# =========================================
# ABA 3 — FEEDBACK
# =========================================

with aba3:

    st.markdown('<div class="feedback-box">', unsafe_allow_html=True)

    st.header("📊 Feedback do Sistema")

    nota_reflexao = st.slider(
        "A IA ajudou você a refletir melhor?",
        1,
        5
    )

    nota_contexto = st.slider(
        "Os exemplos contextualizados ajudaram?",
        1,
        5
    )

    nota_engajamento = st.slider(
        "Você se sentiu mais engajado?",
        1,
        5
    )

    comentario = st.text_area(
        "Comentários adicionais"
    )

    st.button("Enviar Feedback")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.title("⚙️ Configurações")

    modelo = st.selectbox(
        "Modelo IA",
        [
            "GPT-4.1-mini",
            "GPT-4o-mini"
        ]
    )

    modo = st.selectbox(
        "Modo pedagógico",
        [
            "Socrático",
            "Freireano",
            "Reflexivo"
        ]
    )

    profundidade = st.slider(
        "Profundidade das perguntas",
        1,
        5,
        3
    )

    st.markdown("---")

    st.markdown(
        """
        ### Sobre

        Projeto de TCC utilizando:

        - Streamlit
        - OpenAI API
        - IA Educacional
        - Maiêutica
        - Paulo Freire
        """
    )