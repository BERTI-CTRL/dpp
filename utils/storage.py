import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import final
import pandas as pd
#storage.py 


csv_perfis = Path(__file__).parents[1]/'dados'/'perfis.csv'
csv_feedback = Path(__file__).parents[1]/'dados'/'feedback.csv'
csv_conversas = Path(__file__).parents[1]/'dados'/'conversas.csv'
########################################################################

def salvar_perfil(
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

    path_csv_perfis = (
        Path(__file__).parents[1]
        / 'dados'
        / 'perfis.csv'
    )

    path_csv_perfis.parent.mkdir(
        exist_ok=True
    )

    perfil_aluno_novo = pd.DataFrame([{
        'nome': nome,
        'idade': idade,
        'curso': curso,
        'hobbies': ', '.join(hobbies),
        'dificuldade': dificuldade,
        'tema': tema,
        'objetivo': objetivo,
        'tempo_estudo': tempo_estudo,
        'maior_dificuldade': maior_dificuldade,
        'aprende_melhor': ', '.join(aprende_melhor),
        'emocional': emocional,
        'estilo_resposta': estilo_resposta
    }])

    if path_csv_perfis.exists():

        antigo_perfis_csv = pd.read_csv(
            path_csv_perfis
        )

        final = pd.concat(
            [antigo_perfis_csv, perfil_aluno_novo],
            ignore_index=True
        )

    else:

        final = perfil_aluno_novo

    final.to_csv(
        path_csv_perfis,
        index=False
    )
        
    
    final.to_csv(path_csv_perfis,index=False)

    
########################################################################
def salvar_conversa(session_id, nome,pergunta,resposta):
    data_atual = datetime.now()
    path_csv_conversas = Path(__file__).parents[1]/'dados'/'conversas.csv'
    csv_conversas.parent.mkdir(exist_ok=True)


    celula_de_chat = pd.DataFrame([{'nome':nome,
                                  'pergunta':pergunta,
                                  'resposta':resposta,
                                  'session_id':session_id,
                                  'data':data_atual}])
    
    if path_csv_conversas.exists():
        csv_conversas_antigo = pd.read_csv(path_csv_conversas)
        final  = pd.concat([csv_conversas_antigo,celula_de_chat],ignore_index=True)

    else:
        final = celula_de_chat
    
    final.to_csv(path_csv_conversas,index=False)

########################################################################

def salvar_feedback(nota_reflexao,nota_contexto,nota_engajamento,comentarios,session_id):
    feedback_novo = pd.Dataframe([{'nota_reflexao':nota_reflexao,
                                  'nota_contexto':nota_contexto,
                                  'nota_engajamento':nota_engajamento,
                                  'comentarios':comentarios,
                                  'session_id':session_id}])
    
    path_csv_feedback = (
    Path(__file__).parents[1]
    / 'dados'
    / 'feedback.csv'
    )
    path_csv_feedback = path_csv_feedback.parent.mkdir(exist_ok=True)

    if path_csv_feedback.exists():
        csv_feedback_antigo = pd.read_csv(path_csv_feedback)
        final = pd.concat([csv_feedback_antigo,feedback_novo],ignore_index=True)    

    else:
        final = feedback_novo
    
    final.to_csv(path_csv_feedback,index=False)


######################################################################## 
    


def carregar_conversas(path_csv_conversas):
    try:    

        return pd.read_csv(path_csv_conversas)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"O arquivo {path_csv_conversas} não pôde ser encontrado. Verifica carregar_conversas() em storage.py") from e
    
    
    


######################################################################## 

def carregar_perfis(path_perfis_csv):
        
    try:    

        return pd.read_csv(path_perfis_csv)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"O arquivo {path_perfis_csv} não pôde ser encontrado. Verifica carregar_perfis(() em storage.py") from e
    
    
    