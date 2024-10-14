arq = open("pesos.log", "r")
soma = 0
tam = 0

for linha in arq:
    soma += float(linha.split()[1])
    tam += 1

media = soma / tam

print(f"Média de pesos: {media}")

arq.close()