arq = open("financeiro.log", "a")

valor = input("Digite o valor: ")
descricao = input("Digite a descrição: ")

print(valor, descricao, file = arq)

arq.close()