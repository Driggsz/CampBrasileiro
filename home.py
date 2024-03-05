import streamlit as st
import pandas as pd



df = pd.read_csv('copa_brasil.csv')


# Visualiação dos dados
st.dataframe(df)



# Título da página
st.title('Análise de Dados do Brasileirão e Copa do Brasil')


# Divisor
st.markdown('---')

# Prós e contras de usar dados da Copa do Brasil
st.subheader('Prós e Contras de Usar Dados da Copa do Brasil:')

# Prós
st.write('**Prós:**')
st.write('- **Relevância Atualizada:** Os dados da Copa do Brasil apesar de termos menos dadods são mais recentes, refletindo melhor as tendências atuais.')
st.write('- **Torneio Mata-Mata:** Fornece informações sobre o desempenho das equipes em situações de alta pressão.')
st.write('- **Menos Dados Ausentes:** Menos probabilidade de dados ausentes ou desatualizados.')

# Contras
st.write('**Contras:**')
st.write('- **Limitação Temporal:** Os dados são limitados a partir de 2020, reduzindo análises históricas.')
st.write('- **Menos Amostras:** Menor quantidade de dados disponíveis devido ao mata-mata ter uma carga menor de jogos e a base de dados cobrir de 2020 para cá.')
st.write('- **Maior Fator de Imprevisibilidade:** A imprevisibilidade é maior em torneios mata-mata.')