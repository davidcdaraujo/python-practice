import streamlit as st

st.title("Inversor de string")

x = st.text_input("String original: ")

y = x[::-1]

st.write(f"String invertida: {y}")