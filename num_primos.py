def primo(num):
    if num %2 == 0:
        return False
    elif num %3 == 0:
        return False
    elif num %5 == 0:
        return False
    elif num %7 == 0:
        return False
    elif num %11 == 0:
        return False
    elif num %13 == 0:
        return False
    elif num %17 == 0:
        return False
    else:
        return 'Primo'


print('Informe um número maior que 20')
x = int(input('Número: '))
print(primo(x))