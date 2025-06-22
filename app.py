import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="BrasilStatics Deep", layout="wide")
st.title("⚽ BrasilStatics Deep - Análises em Tempo Real")

# Dados de exemplo (substitua pelo link da SUA planilha depois)
dados = {
    "Jogo": ["Flamengo x Palmeiras", "Corinthians x São Paulo"],
    "Placar": ["2-1", "0-0"],
    "Escanteios": [5, 3],
    "Finalizações": [12, 8]
}

# Sidebar
st.sidebar.header("Filtros")
time_selecionado = st.sidebar.selectbox("Escolha um time:", list(set([jogo.split(' x ')[0] for jogo in dados["Jogo"])))

# Tabela principal
st.header("📊 Estatísticas dos Jogos")
df = pd.DataFrame(dados)
st.dataframe(df[df["Jogo"].str.contains(time_selecionado)])

# Link para edição
st.markdown("""
🔧 **Como atualizar os dados?**  
1. Acesse a [Planilha Google](https://bit.ly/brasilstatics-sheet)  
2. Faça uma cópia (File > Make a copy)  
3. Adicione seus dados manualmente  
""")
