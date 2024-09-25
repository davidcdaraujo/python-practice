def maior(lista):

    return f"{max(lista)} é o maior número"


num = []

for i in range(3):
    x = float(input("Número: "))
    num.append(x)

print(maior(num))