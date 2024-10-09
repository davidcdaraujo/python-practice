#COM BIBLIOTECA NUMPY
import numpy as np

m1 = np.array([[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]])
m2 = np.array([[5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8]])

print("SOMA DAS MATRIZES:")
x = m1 + m2
for i in x:
    print(i)

print("SUBTRAÇÂO DAS MATRIZES:")
y = m1 - m2
for i in y:
    print(i)

#COM LÓGICA
'''res = []

for i in range(len(m1)):
    linha = []
    for j in range(len(m1[0])):
        linha.append(m1[i][j] + m2[i][j])
    res.append(linha)

for i in res:
    print(i)'''