while True:
    x = input("Começar programa (s/n)? ")
    y = x.lower()

    if y == "s":

        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
    
        while nota1 < 0 or nota1 > 10:
            print("Insira uma nota 1 válida, entre 0 e 10")
            nota1 = float(input("Nota 1: "))

        while nota2 < 0 or nota2 > 10:
            print("Insira uma nota 2 válida, entre 0 e 10")
            nota2 = float(input("Nota 2: "))

        print("Resultado:", (nota1 + nota2) / 2)
    
    elif y == "n":
        print("Programa encerrado.")
        break