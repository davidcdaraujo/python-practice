def romano(str):
    valor = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    anterior = 0
    
    for i in str[::-1]:
        atual = valor[i]
        
        if atual < anterior:
            total -= atual
        else:
            total += atual

        anterior = atual
    return total


x = "VIIX"
print(f'{x} = {romano(x)}')