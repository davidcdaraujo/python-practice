arq = open("financeiro.log", "r")

for linha in arq:
     print(linha)

arq.close()