m = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Número: ")))
    m.append(linha)

print("---------")   
for i in m:
    print(i)
print("---------")

num = int(input("Verificar se está na matriz: "))
contido = False

for i in m:
    for j in i:
        if j == num:
            contido = True
            break

if contido:
    print("Contido")
else:
    print("Não contido")