def dna(string):

    y = string.upper()
    convertido = ''

    for i in y:
        if i == 'A':
            convertido += 'T'
        elif i == 'T':
            convertido += 'A'
        elif i == 'C':
            convertido += 'G'
        elif i == 'G':
            convertido += 'C'
    return convertido


x = input("Insira seu código genético: ")
print(f'DNA original: {x.upper}')
print('Convertido:', dna(x))