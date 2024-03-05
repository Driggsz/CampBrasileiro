import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache_data
def load_data():
    df = pd.read_csv(r'D:\copadobrasil\pages\brasileirao.csv')  # Especifique o caminho do arquivo corretamente
    return df

df = load_data()

# Visualização dos dados
st.dataframe(df)


# Título da página
st.title('Análise de Dados do Brasileirão')

st.markdown('---')


# Prós
st.write('**Prós:**')
st.write('- **Ampla Disponibilidade de Dados:** Dados disponíveis desde 2003 para análises históricas.')
st.write('- **Maior Número de Amostras:** Grande quantidade de dados disponíveis devido ao formato de liga com vários jogos disputados.')

# Contras
st.write('**Contras:**')
st.write('- **Dados Ausentes ou Desatualizados:** Possibilidade de dados ausentes ou desatualizados, especialmente em períodos mais antigos.')
st.write('- **Variações de Formato de Liga:** Mudanças no formato do campeonato ao longo dos anos podem introduzir variações nos dados.')
