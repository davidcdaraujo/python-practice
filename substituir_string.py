def substituir(i, antiga, novo):
    resultado = ''
    for letra in i:
        if letra == antiga:
            resultado += novo
        else:
            resultado += letra
    return resultado

frase = 'Buracos negros são massas de pesos inimagináveis.'
letraantiga = ' '
letranova = '#'

novafrase = substituir(frase, letraantiga, letranova)
print(novafrase)