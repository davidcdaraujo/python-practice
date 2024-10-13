arq = open("financeiro.log", "r")
saldo = 0

for linha in arq:
    saldo += int(linha.split()[0])

print("Saldo =", saldo)

arq.close()