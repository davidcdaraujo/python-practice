def data(a, b, c):
    print(a,'/',b,'/',c)
    if b == '01':
        print(f'Hoje é dia {a} de janeiro de {c}.')
    elif b == '02':
        print(f'Hoje é dia {a} de fevereiro de {c}.')
    elif b == '03':
        print(f'Hoje é dia {a} de março de {c}.')
    elif b == '04':
        print(f'Hoje é dia {a} de abril de {c}.')
    elif b == '05':
        print(f'Hoje é dia {a} de maio de {c}.')
    elif b == '06':
        print(f'Hoje é dia {a} de junho de {c}.')
    elif b == '07':
        print(f'Hoje é dia {a} de julho de {c}.')
    elif b == '08':
        print(f'Hoje é dia {a} de agosto de {c}.')
    elif b == '09':
        print(f'Hoje é dia {a} de setembro de {c}.')
    elif b == '10':
        print(f'Hoje é dia {a} de outubro de {c}.')
    elif b == '11':
        print(f'Hoje é dia {a} de novembro de {c}.')
    elif b == '12':
        print(f'Hoje é dia {a} de dezembro de {c}.')    


x = input('Dia: ')
y = input('Mês: ')
z = input('Ano: ')
data(x, y, z)