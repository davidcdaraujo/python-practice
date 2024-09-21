def inverte(frase):
    palavras = frase.split()
    z = palavras[::-1]
    
    invertida = ''
    for i in range(len(z)):
        invertida += z[i]
        if i < len(z) - 1:
            invertida += ' '
    print(invertida)


inverte('Comi pão no café da manhã.')