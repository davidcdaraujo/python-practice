m = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input("Número: ")))
    m.append(linha)

print("MATRIZ INICIAL:")
for i in m:
    print(i)

x = int(input("Multiplicar a matriz principal por: "))

print("MATRIZ FINAL:")
for i in range(4):
    m[i][i] *= x

for i in m:
    print(i)