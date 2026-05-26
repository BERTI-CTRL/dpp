# Interface Streamlit — TCC IA Socrática

import streamlit as st

from pathlib import Path
import os
import pandas as pd

from utils.render import (
    renderizar_resposta
)

from utils.storage import (
    salvar_perfil,
    salvar_conversa,
    salvar_feedback,
    carregar_perfis,
    carregar_conversas
)

from utils.prompts import (
    carregar_prompt,
    montar_contexto_perfil,
    montar_memoria
)

from utils.ia import (
    gerar_resposta
)
from utils.session import (
    gerar_session_id
)

from datetime import datetime   

# =========================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================

st.set_page_config( 
    page_title="Tutor Socrático IA",
    page_icon="🧠",
    layout="wide"
)

if Path('.env').exists():

    openai_key = os.getenv("OPENAI_API_KEY")

else:
    
    openai_key = st.secrets["OPENAI_API_KEY"]

if Path('.env').exists():

    gemini_key = os.getenv("GEMINI_API_KEY")

else:
    
    gemini_key = st.secrets["GEMINI_API_KEY"]







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





with st.sidebar:

    st.title("⚙️ Configurações")

    modelo = st.selectbox(
                            "Modelo IA",
                                        [
                            "gpt-4o-mini",
                            "gemini-3.1-flash-lite"
                                        ]
)
    

    modo = st.selectbox(
        "Modo pedagógico",
        [
            "Socrático",
            "Freireano"
            
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



if "perfil_contexto" not in st.session_state:
    st.session_state.perfil_contexto = ""

if "memoria_pedagogica" not in st.session_state:
    st.session_state.memoria_pedagogica = {
        "conceitos_compreendidos": [],
        "conceitos_dificuldade": [],
        "hipoteses": []
    }



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

    st.markdown(
        '<div class="perfil-box">',
        unsafe_allow_html=True
    )

    st.header("👤 Perfil do Estudante")

    st.markdown(
        """
        Essas informações ajudam a IA a adaptar
        explicações, exemplos e perguntas de acordo
        com sua realidade e forma de aprender.
        """
    )

    col1, col2 = st.columns(2)

    # =========================================
    # COLUNA 1
    # =========================================

    with col1:

        nome = st.text_input("Nome")

        idade = st.number_input(
            "Idade",
            min_value=10,
            max_value=100
        )

        curso = st.text_input(
            "Curso / Série"
        )

        tema = st.text_input(
            "Tema que deseja estudar"
        )

        objetivo = st.selectbox(
            "Qual seu principal objetivo?",
            [
                "Vestibular",
                "ENEM",
                "Prova escolar",
                "Faculdade",
                "Curiosidade",
                "Aprender por interesse pessoal",
                "Melhorar notas",
                "Outro"
            ]
        )

        tempo_estudo = st.selectbox(
            "Quanto tempo costuma estudar por dia?",
            [
                "Menos de 30 minutos",
                "30 minutos",
                "1 hora",
                "2 horas",
                "Mais de 2 horas"
            ]
        )

    # =========================================
    # COLUNA 2
    # =========================================

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
                "Filosofia",
                "Robótica",
                "Psicologia"
            ]
        )

        dificuldade = st.selectbox(
            "Nível de dificuldade no tema",
            [
                "Iniciante",
                "Intermediário",
                "Avançado"
            ]
        )

        maior_dificuldade = st.text_area(
            "Qual sua maior dificuldade ao estudar esse tema?"
        )

        aprende_melhor = st.multiselect(
            "Como você aprende melhor?",
            [
                "Exemplos práticos",
                "Passo a passo",
                "Exercícios",
                "Analogias",
                "Vídeos",
                "Discussão/conversa",
                "Teoria",
                "Com perguntas que me façam pensar",

            ]
        )

        emocional = st.selectbox(
            "Como você se sente em relação a esse tema?",
            [
                "Muito confiante",
                "Confiante",
                "Neutro",
                "Inseguro",
                "Muito inseguro",
                "Ansioso"
            ]
        )

        estilo_resposta = st.selectbox(
            "Como prefere as respostas da IA?",
            [
                "Mais diretas",
                "Mais reflexivas",
                "Passo a passo",
                "Com exemplos do cotidiano",
                "Com perguntas guiadas"
            ]
        )

    

    if st.button("Salvar Perfil"):
        timestamp = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        salvar_perfil(
            st.session_state.session_id,
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
        )

        st.session_state.perfil_contexto = {
                                            "nome": nome,
                                            "idade": idade,
                                            "curso": curso,
                                            "hobbies": hobbies,
                                            "dificuldade": dificuldade,
                                            "tema": tema,
                                            "objetivo": objetivo,
                                            "tempo_estudo": tempo_estudo,
                                            "maior_dificuldade": maior_dificuldade,
                                            "aprende_melhor": aprende_melhor,
                                            "emocional": emocional,
                                            "estilo_resposta": estilo_resposta
                                            }



        st.success("Perfil salvo com sucesso!")

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )










# =========================================
# ABA 2 — CHAT IA
# =========================================

with aba2:

    st.markdown(
        '<div class="chat-box">',
        unsafe_allow_html=True
    )

    st.header("💬 Conversa com a IA")

    if "session_id" not in st.session_state:

        st.session_state.session_id = (
            gerar_session_id()
        )

    if "numero_interacao" not in st.session_state:

        st.session_state.numero_interacao = 0

    if "messages" not in st.session_state:

        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

    prompt = st.chat_input(
        "Digite sua pergunta..."
    )

    if prompt:

        st.session_state.numero_interacao += 1

        with st.chat_message(
            "user"
        ):

            st.markdown(prompt)

        # =====================================
        # SYSTEM PROMPT
        # =====================================

        system_prompt = carregar_prompt(
            modo
        )

        # =====================================
        # PROFUNDIDADE
        # =====================================

        profundidade_contexto = {

            1:
            """
            Respostas diretas.
            Faça no máximo uma pergunta reflexiva.
            """,

            2:
            """
            Misture explicação e reflexão.
            Faça perguntas ocasionais.
            """,

            3:
            """
            Equilibre explicação e questionamento.
            Estimule o raciocínio do estudante.
            """,

            4:
            """
            Priorize perguntas guiadas.
            Evite entregar respostas prontas rapidamente.
            """,

            5:
            """
            Atue fortemente pela maiêutica.
            Questione hipóteses.
            Conduza a construção do raciocínio.
            """
        }

        # =====================================
        # PERFIL
        # =====================================

        perfil_contexto = (
            montar_contexto_perfil(
                st.session_state.perfil_contexto
            )
        )

        # =====================================
        # MEMÓRIA
        # =====================================

        memoria_contexto = (
            montar_memoria(
                st.session_state.memoria_pedagogica
            )
        )

        # =====================================
        # MENSAGENS PARA IA
        # =====================================

        messages_api = [

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "system",
                "content":
                profundidade_contexto[
                    profundidade
                ]
            },

            {
                "role": "system",
                "content": perfil_contexto
            },

            {
                "role": "system",
                "content": memoria_contexto
            }
        ]

        messages_api.extend(
            st.session_state.messages
        )

        messages_api.append(

            {
                "role": "user",
                "content": prompt
            }
        )

        # =====================================
        # RESPOSTA IA
        # =====================================

        with st.chat_message(
            "assistant"
        ):

            with st.spinner(
                "Pensando..."
            ):

                try:

                    resposta_ia = (
                        gerar_resposta(

                            modelo=modelo,

                            messages=
                            messages_api
                        )
                    )

                except Exception as e:

                    resposta_ia = (
                        f"Erro na IA: {e}"
                    )

            renderizar_resposta(
                                resposta_ia
                                )

        # =====================================
        # HISTÓRICO
        # =====================================

        st.session_state.messages.append(

            {
                "role": "user",
                "content": prompt
            }
        )

        st.session_state.messages.append(

            {
                "role": "assistant",
                "content": resposta_ia
            }
        )

        # =====================================
        # MEMÓRIA PEDAGÓGICA
        # =====================================

        st.session_state.memoria_pedagogica[
            "hipoteses"
        ].append(
            prompt
        )

        st.write(
        st.session_state.memoria_pedagogica
        )
        # =====================================
        # SALVAR
        # =====================================

        salvar_conversa(

            session_id=
            st.session_state.session_id,

            numero_interacao=
            st.session_state.numero_interacao,

            nome=nome,

            pergunta=prompt,

            resposta=resposta_ia,

            modelo=modelo,

            modo=modo,

            profundidade=profundidade
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )










# =========================================
# ABA 3 — FEEDBACK
# =========================================

with aba3:

    st.markdown('<div class="feedback-box">', unsafe_allow_html=True)

    st.header("📊 Feedback da Experiência")

    st.markdown(
        """
        Sua opinião é importante para avaliar se a IA
        realmente contribui para uma aprendizagem
        mais reflexiva e crítica.
        """
    )

    # =========================================
    # REFLEXÃO E PENSAMENTO CRÍTICO
    # =========================================

    st.subheader("🧠 Reflexão e pensamento crítico")

    nota_reflexao = st.slider(
        "A IA ajudou você a refletir melhor sobre o conteúdo?",
        1,
        5,
        3
    )

    nota_pensamento = st.slider(
        "As perguntas da IA fizeram você pensar antes de responder?",
        1,
        5,
        3
    )

    nota_autonomia = st.slider(
        "Você sentiu que construiu o raciocínio por conta própria?",
        1,
        5,
        3
    )

    # =========================================
    # CONTEXTUALIZAÇÃO
    # =========================================

    st.subheader("🌍 Contextualização")

    nota_contexto = st.slider(
        "Os exemplos contextualizados ajudaram na compreensão?",
        1,
        5,
        3
    )

    nota_cotidiano = st.slider(
        "A IA conseguiu relacionar o conteúdo ao seu cotidiano?",
        1,
        5,
        3
    )

    # =========================================
    # ENGAJAMENTO
    # =========================================

    st.subheader("🎯 Engajamento")

    nota_engajamento = st.slider(
        "Você se sentiu mais engajado durante a conversa?",
        1,
        5,
        3
    )

    nota_interesse = st.slider(
        "A conversa despertou mais interesse pelo tema estudado?",
        1,
        5,
        3
    )

    # =========================================
    # COMPARAÇÃO COM IA TRADICIONAL
    # =========================================

    st.subheader("🤖 Comparação com outras IAs")

    comparacao = st.radio(
        "Comparada a IAs que apenas dão respostas prontas, esta experiência foi:",
        [
            "Muito pior",
            "Pior",
            "Sem diferença",
            "Melhor",
            "Muito melhor"
        ]
    )

    # =========================================
    # DIFICULDADE E FRUSTRAÇÃO
    # =========================================

    st.subheader("⚖️ Dificuldade")

    nota_dificuldade = st.slider(
        "As perguntas da IA foram difíceis em excesso?",
        1,
        5,
        3
    )

    nota_frustracao = st.slider(
        "Você se sentiu frustrado em algum momento da interação?",
        1,
        5,
        1
    )

    # =========================================
    # RESPOSTAS ABERTAS
    # =========================================

    st.subheader("✍️ Respostas abertas")

    aprendizado = st.text_area(
        "O que você acredita ter aprendido ou compreendido melhor?"
    )

    experiencia = st.text_area(
        "Como você descreveria a experiência de conversar com essa IA?"
    )

    sugestoes = st.text_area(
        "Sugestões, críticas ou melhorias"
    )

    # =========================================
    # BOTÃO
    # =========================================

    if st.button("Enviar Feedback"):
        salvar_feedback(

            session_id = st.session_state.session_id,

            modelo = modelo,

            modo = modo,

            profundidade = profundidade,

            nota_reflexao = nota_reflexao,

            nota_pensamento = nota_pensamento,

            nota_autonomia = nota_autonomia,

            nota_contexto = nota_contexto,

            nota_cotidiano = nota_cotidiano,

            nota_engajamento = nota_engajamento,

            nota_interesse = nota_interesse,

            nota_dificuldade = nota_dificuldade,

            nota_frustracao = nota_frustracao,

            comparacao = comparacao,

            aprendizado =  aprendizado,

            experiencia = experiencia,

            sugestoes = sugestoes



        )

        st.success("Feedback enviado com sucesso!")

    st.markdown('</div>', unsafe_allow_html=True)




# =========================================
# SIDEBAR
# =========================================

