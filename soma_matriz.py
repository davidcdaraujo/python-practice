m = [
    [1, 1, 1, 1], 
    [2, 2, 2, 2], 
    [3, 3, 3, 3], 
    [4, 4, 4, 4]
]
print(m)

x = sum(m[2]) #soma da linha 3
print(f"Soma da linha 3: {x}")

coluna = 1
soma = sum(i[coluna] for i in m) #soma da coluna 2
print(f"Soma da coluna 2: {soma}")

total = 0

for i in m:
    for j in i:
        total += j       
print(f"Soma de todos os elementos: {total}")