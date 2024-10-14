arq = open("alturas.log", "r")
lista = []

for linha in arq:
    altura = float(linha.split()[1])
    lista.append(altura)

print(f"Maior altura: {max(lista)}")

arq.close()