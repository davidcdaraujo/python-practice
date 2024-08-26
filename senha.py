senha = input("Senha: ")

while senha != "teste":
    print("ACESSO NEGADO")
    senha = input("Senha: ")

    if senha == "teste":
        print("ACESSO PERMITIDO")