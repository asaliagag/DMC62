import streamlit as st

st.tittle("Especialización Python for analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Andrea Aliaga")

modulos = st.selectbox("Selecione el módulo",["Listas", "Arreglos", "Funciones", "POO"])
