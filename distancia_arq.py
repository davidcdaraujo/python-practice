arq = open("distancia.log", "r")
lista = []

for linha in arq:
    distancia = int(linha.split()[2])
    lista.append(distancia)

print(f"Maior distância: {max(lista)}")

arq.close()