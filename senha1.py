contar = 0
senha = input("Senha: ")

if senha == "teste":
    print("ACESSO PERMITIDO")

while senha != "teste":

    print("ACESSO NEGADO")
    contar += 1
    senha = input("Senha: ")

    if senha == "teste":

        print("ACESSO PERMITIDO")
        print(f"Tentativas: {contar}")