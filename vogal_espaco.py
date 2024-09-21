def espaco(frase):
    contador = 0
    vogal = 0
    
    for i in range(len(frase)):
        if frase[i] == ' ':
            contador += 1
    print(f'A frase possui {contador} espaço(s).')                  #NAO CONTA VOGAL COM ACENTO
    
    for i in range(len(frase)):
        x = frase.lower()
        if x[i] == 'a':
            vogal += 1
        if x[i] == 'e':
            vogal += 1
        if x[i] == 'i':
            vogal += 1
        if x[i] == 'o':
            vogal += 1
        if x[i] == 'u':
            vogal += 1
    print(f'A frase possui {vogal} vogal(s).')


y = input('Digite uma frase: ')
espaco(y)