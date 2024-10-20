import streamlit as st

st.title("Cálculo de potência")

x = st.number_input("Base: ")
y = st.number_input("Expoente: ")

res = x**y

st.write(f"Resultado: {res}")