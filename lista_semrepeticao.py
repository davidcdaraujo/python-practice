def remover(x):
    listanova = []
    for i in x:
        if i not in listanova:
            listanova.append(i)
    return(listanova)


lista = [1, 3, 4, 2, 7, 7, 7, 2, 2, 4]
print(remover(lista))