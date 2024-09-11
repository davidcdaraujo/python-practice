def binario(decimal):
    lista = []

    while decimal > 0:
        x = decimal % 2
        lista.append(x)
        decimal = decimal // 2
    lista.reverse()
    return (f'Número em binário: {lista}')


y = int(input('Digite um número decimal: '))
print(binario(y))