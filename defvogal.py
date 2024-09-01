def count(x):

    y = "AEIOUaeiouáàéêãâíóôõúûùÀÁÉÂÈÊÃÍÌÒÓÚ"
    contar = 0

    for i in range(len(x)):
        if x[i] in y:
            contar += 1
    
    return contar


texto = input("Texto: ")
print(f"O texto possui {count(texto)} vogais.")