import re
import streamlit as st


import re
import streamlit as st

def renderizar_resposta(texto):

    padrao = r'\\\[(.*?)\\\]'

    partes = re.split(
        padrao,
        texto,
        flags=re.DOTALL
    )

    for i, parte in enumerate(partes):

        if i % 2 == 0:

            if parte.strip():

                st.markdown(parte)

        else:

            st.latex(
                parte.strip()
            )