gols = []
cuiaba = 0
mixto = 0

while True:

    comando = input("Contar([s]im)/Encerrar([n]ão): ")

    if comando == "s":

        x = int(input("Gol do Mixto(1)/Gol do Cuiabá(2): "))
        y = gols.append(x)

        if x == 1:
            mixto += 1
        elif x == 2:
            cuiaba += 1

    elif comando == "n":

        if mixto > cuiaba:
            print(f"Mixto [{mixto}]X[{cuiaba}] Cuiabá, Mixto ganhou!")
        elif cuiaba > mixto:
            print(f"Cuiabá [{mixto}]X[{cuiaba}] Mixto, Cuiabá ganhou!")
        elif mixto == cuiaba:
            print(f"Cuiabá [{mixto}]X[{cuiaba}] Mixto, EMPATE!")

        print("Programa encerrado.")
        break