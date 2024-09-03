import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

import streamlit as st

# Carregamento do dataset
df = pd.read_csv('dataset/imigrantes_canada.csv')

# PROCESSAMENTO E TRATAMENTO DE DADOS 
df_index_pais = df.set_index('País')  # Define 'País' como índice
brasil = df_index_pais.loc['Brasil']  # Seleciona a linha Brasil como uma Série

# Reseta o índice e transforma a série em um DataFrame (opcional, se precisar de visualização)
brasil = brasil.reset_index()

# Agora, remova as duas primeiras linhas (supondo que queira remover as primeiras linhas com base na posição)
brasil = brasil.iloc[2:]

# Se precisar voltar a ter um índice sequencial
brasil = brasil.reset_index(drop=True)

brasil = brasil[brasil.index != 34]  # retirando a linha de número 34 que se refere ao total de imigrantes 
brasil.columns = ["Ano", "Imigrantes"]
x = brasil['Ano']
y = brasil['Imigrantes']

# Treinamento do modelo
modelo = LinearRegression()
x = brasil[["Ano"]]
y = brasil[["Imigrantes"]]
modelo.fit(x, y)

# Site Streamlit
st.image("foto/imagem.webp")
st.title("Previsão de imigração do Brasil para o Canadá")
st.divider()

ano = st.number_input("Digite o Ano que você deseja prever:", step=1, format="%d")

if ano:
    imigrantes_previstos = modelo.predict([[ano]])[0][0]
    st.write(f" Para o ano de : {ano:.0f} a previsão é de : {imigrantes_previstos:.0f} imigrantes saindo do Brasil para o Canadá.")
    st.balloons()
