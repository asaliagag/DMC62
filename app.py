import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Andrea Aliaga")

modulos = st.selectbox("Selecione el módulo",["Listas", "Arreglos", "Funciones", "POO"])
