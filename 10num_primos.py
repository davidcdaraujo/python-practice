def primos(x):
    lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if x == 1:
        x = lista
    return(x)


print('Digite 1 para ver uma lista dos 10 primeiros números primos')
y = int(input())
print(primos(y))