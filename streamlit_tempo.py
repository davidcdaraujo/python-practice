import streamlit as st

st.title("Média de tempo de viagem")

def tempo(dis, vel):
    res = dis / vel
    return res


x = st.number_input("Distância: ")
y = st.number_input("Velocidade: ")

st.write(f"Média: {tempo(x, y)}")