def soma(lista):

    return sum(lista)


num = []

for i in range(5):
    x = int(input("Número: "))
    num.append(x)

print(num)
print(f"Soma: {soma(num)}")