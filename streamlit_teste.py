import streamlit as st

def par(num):
    if num % 2 == 0:
        st.write("Par")
    else:
        st.write("Ímpar")


n = st.number_input("Número: ")
par(n)