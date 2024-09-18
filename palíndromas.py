def palindroma(a, b):
    if a == b[::-1]:
        print(f'{a} e {b} são palavras palíndromas.')
    else:
        print(f'{a} e {b} não são palavras palíndromas.')

x = input('Digite uma palavra: ')
y = input('Digite outra palavra: ')
palindroma(x, y)