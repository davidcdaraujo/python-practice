arq = open("gastos.log", "r")
soma = 0

for linha in arq:
    soma += int(linha.split()[1])

print(f"Total de gastos: {soma}")

arq.close()