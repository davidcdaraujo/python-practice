arq = open("compras.log", "r")
lista = []

for linha in arq:
    compra = float(linha.split()[2])
    lista.append(compra)

print(f"Média de compras: {sum(lista) / len(lista)}")

arq.close()