def vogais(frase):
    lista = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú']
    contador = 0
    y = frase.lower()
    for i in y:
        if i in lista:
            contador += 1
    return contador


x = '29 de fevereiro só aparece em anos bissextos'
print(f'A frase possui {vogais(x)} vogais.')