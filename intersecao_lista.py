def interseção(x, y):
    lista = []
    for i in x:
        if i in y:
            lista.append(i)
    return(lista)


a = [1, 3, 4, 2, 5]
b = [1, 9, 2, 6, 4]
print(interseção(a, b))