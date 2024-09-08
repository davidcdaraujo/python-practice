lista = []

while True:

    num = int(input("Número: "))
    
    if num <= 0:
        break

    lista.append(num)

print(f"Lista de números: {lista}")
print(f"Maior número: {max(lista)}")
print(f"Menor número: {min(lista)}")