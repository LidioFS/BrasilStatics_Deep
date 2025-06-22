import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuração da página
st.set_page_config(page_title="BrasilStatics Deep", layout="wide")
st.title("⚽ BrasilStatics Deep - Análise em Tempo Real")

# Conexão com sua planilha
def conectar_planilha():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
    client = gspread.authorize(creds)
    
    # Substitua pelo ID da SUA planilha (encontre na URL: docs.google.com/spreadsheets/d/[ID]/edit)
    planilha = client.open_by_key("1yhyMzq6QY-7n7Z4X7Q8W6TzJ9Xb1v2y5mHj3K8L9N0P")
    return planilha.sheet1

# Interface
try:
    sheet = conectar_planilha()
    dados = sheet.get_all_records()
    df = pd.DataFrame(dados)

    # Sidebar
    st.sidebar.header("Filtros")
    times = list(set([jogo['Jogo'].split(' x ')[0] for jogo in dados if 'Jogo' in jogo))
    time_selecionado = st.sidebar.selectbox("Selecione um time:", times)

    # Dados filtrados
    st.header(f"Estatísticas para {time_selecionado}")
    st.dataframe(df[df['Jogo'].str.contains(time_selecionado)])

    # Gráfico de escanteios
    st.bar_chart(df[['Jogo', 'Escanteios']].set_index('Jogo'))

except Exception as e:
    st.error(f"Erro ao carregar dados: {str(e)}")
    st.info("""
    🔧 Verifique:
    1. Se o arquivo 'credenciais.json' está no diretório
    2. Se a planilha está compartilhada com o e-mail do serviço
    3. Se a estrutura de dados está igual ao modelo
    """)
