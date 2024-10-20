import streamlit as st

st.title("Divisão de despesas")

x = st.number_input("Total da conta: ")
y = st.number_input("Total de pessoas: ")

if st.button("Resultado"):
    resultado = x / y
    st.write(f"{resultado} reais para cada")