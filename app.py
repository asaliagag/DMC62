import streamlit as st
import numpy as np

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Andrea aliaga")

st.image("Python_logo.png",width =300)
st.sidebar.image("DMC.png")


modulos = st.sidebar.selectbox("Selecione el módulo",["Listas", "Arreglos", "Funciones", "POO"])

if modulos == "Listas":
  st.write("Te encuentras en el módulo de listas")

  valor_inicial = int(st.number_input("Ingresa tu valor inicial del rango", value=0))
  valor_final = int(st.number_input("Ingresa tu valor final del rango",value=10))

  lista = list(range(valor_inicial, valor_final))

  st.write(lista)

elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de arreglos")

  cantidad = st.slider("Seleccione un valor del rango", min_value = 1, max_value = 100, value=20 )
  arreglo = np.arange(cantidad)

  st.write(arreglo)


elif modulos == "Funciones":
  st.write("Te encuentras en el módulo de Funciones")
  
else:
  st.write("Te encuentras en el módulo de POO")
