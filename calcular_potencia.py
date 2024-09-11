print('///CALCULADORA DE POTÊNCIA///')

def calcular(x, y):
    c = 1
    for i in range(y):
        c *= x
    return(c)

a = int(input('Base: '))
b = int(input('Expoente: '))
print(calcular(a, b))