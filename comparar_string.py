x = 'Hoje eu tenho que ir à autoescola.'
y = 'Hoje eu tenho que ir à autoescola.'

print(f'{x}\n{y}')
print(f'"{x}": possui {len(x)} caracteres.\n"{y}": possui {len(y)} caracteres.')

if len(x) == len(y):
    print('As duas strings possuem o mesmo tamanho')
else:
    print('As duas strings possuem tamanhos diferentes')

if x == y:
    print('As duas strings possuem o mesmo conteúdo')
else:
    print('As duas strings possuem conteúdos diferentes')