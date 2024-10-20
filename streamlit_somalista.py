import streamlit as st

st.title("Soma de uma lista")

lista = []

for i in range(3):
    y = st.number_input(f"Número {i+1}: ", key=f"num_{i}")
    lista.append(y)

def soma(num):

    x = sum(num)
    return x


st.write(f"Soma = {soma(lista)}")