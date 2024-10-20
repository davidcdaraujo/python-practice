import streamlit as st

st.title("Maior número")

x = st.number_input("Número1: ")
y = st.number_input("Número2: ")
z = st.number_input("Número3: ")

lista = [x, y, z]

st.write(f"Maior número = {max(lista)}")