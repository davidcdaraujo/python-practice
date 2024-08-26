lista = []
aprovado = 0
reprovado = 0
exame = 0

while True:
    
    x = int(input("1 para continuar/2 para finalizar: "))

    if x == 1:

        nota1 = float(input("Nota 1 do aluno: "))
        nota2 = float(input("Nota 2 do aluno: "))

        media = (nota1 + nota2) / 2
        z = lista.append(media)
        print(f"Média final: {media}")
    
    elif x == 2:

        print(f"Notas: {lista}")

        for i in lista:
            if i >= 7.0:
                aprovado += 1
            elif i < 6:
                reprovado += 1
            elif i < 7 and i >= 6:
                exame += 1

        print(f"Aprovados(s): {aprovado}\nReprovado(s): {reprovado}\nExame: {exame}")

        print("Programa finalizado.")
        break