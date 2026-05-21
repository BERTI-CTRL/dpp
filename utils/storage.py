import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import final
import pandas as pd


'''
def salvar_perfil(...)

def salvar_conversa(...)

def salvar_feedback(...)

def carregar_conversas(...)

def carregar_perfis(...)'''
csv_perfis = Path(__file__).parents[1]/'dados'/'perfis.csv'
csv_feedback = Path(__file__).parents[1]/'dados'/'feedback.csv'
csv_conversas = Path(__file__).parents[1]/'dados'/'conversas.csv'


def salvar_perfil(nome,idade,curso,hobbies,dificuldade,tema):
    path_csv_perfis = Path(__file__).parents[1]/'dados'/'perfis.csv'
    path_csv_perfis.parent.mkdir(exist_ok=True)

    perfil_aluno_novo =pd.DataFrame([{'nome':nome,
                    'idade':idade,
                    'curso':curso,
                    'hobbies':','.join(hobbies),
                    'dificuldade':dificuldade,
                    'tema':tema}])


    if path_csv_perfis.exists():   
        antigo_perfis_csv = pd.read_csv(path_csv_perfis)
        final = pd.concat([antigo_perfis_csv,perfil_aluno_novo],ignore_index=True)
    else:
        final = perfil_aluno_novo
        
    
    final.to_csv(path_csv_perfis,index=False)

    

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



def salvar_feedback(nota_reflexao,nota_contexto,comentarios,session_id):
    feedback = pd.Dataframe({'nota_reflexao':nota_reflexao,
                                  'nota_contexto':nota_contexto,
                                  'comentarios':comentarios,
                                  'session_id':session_id})
    
    


def carregar_conversas(celula_de_chat):


def carregar_perfis(perfis_csv):
    perfis_carregados = pd.read_csv(perfis_csv)
