idades = []

while True:

    x = int(input("Idade: "))
    idades.append(x)

    if x == 0:
        break

idades.remove(0)
print(f"Lista de idades: {idades}")


media = (sum(idades)) / len(idades)
print(f"Média: {media}")

