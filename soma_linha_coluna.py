matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sl = {
    "l1": sum(matriz[0]),
    "l2": sum(matriz[1]),
    "l3": sum(matriz[2])
}

c1 = 0
c2 = 1
c3 = 2

sc = {
    "c1": sum(i[c1] for i in matriz),
    "c2": sum(i[c2] for i in matriz),
    "c3": sum(i[c3] for i in matriz)
}

print(f"Vetor da soma das linhas: {sl}")
print(f"Vetor da soma das colunas: {sc}")