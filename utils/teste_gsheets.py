import gspread

from oauth2client.service_account import (
    ServiceAccountCredentials
)

# =========================================
# ESCOPO
# =========================================

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# =========================================
# CREDENCIAIS
# =========================================

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credenciais.json",
    scope
)

# =========================================
# CLIENTE
# =========================================

client = gspread.authorize(creds)

# =========================================
# ABRIR PLANILHA
# =========================================

planilha = client.open("IA_Educacional")

# =========================================
# ABRIR ABA
# =========================================

aba = planilha.worksheet("perfis")

# =========================================
# ESCREVER
# =========================================

aba.append_row([
    "teste_session",
    "2026-05-25",
    "Aluno Teste",
    20,
    "Engenharia"
])

print("Escreveu na planilha com sucesso.")