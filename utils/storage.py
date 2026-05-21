import os
import shutil
from pathlib import Path
from datetime import datetime
import pandas as pd
'''
def salvar_perfil(...)

def salvar_conversa(...)

def salvar_feedback(...)

def carregar_conversas(...)

def carregar_perfis(...)'''

def salvar_perfil(nome,idade,curso,hobbies,dificuldade,tema)
    perfil_aluno = {'nome':nome,
                    'idade':idade,
                    'curso':curso,
                    'hobbies':hobbies,
                    'dificuldade':dificuldade,
                    'tema':tema}

    return perfil_aluno

def salvar_conversa(session_id, nome,pergunta,resposta):
    data = datetime.now()
    celula_de_chat = pd.Dataframe({'nome':nome,
                                  'pergunta':pergunta,
                                  'resposta':resposta,
                                  'session_id':session_id})
    
    csv_conversas = pd.to



def salvar_feedback(nota_reflexao,nota_contexto,comentarios,session_id):
    feedback = pd.Dataframe({'nota_reflexao':nota_reflexao,
                                  'nota_contexto':nota_contexto,
                                  'comentarios':comentarios,
                                  'session_id':session_id})
    
    


def carregar_conversas(celula_de_chat):


def carregar_perfis(...):