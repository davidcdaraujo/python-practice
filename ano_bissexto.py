def bissexto(ano):
    if ano %4 == 0 and ano %100 != 0:
        return True
    elif ano %400 == 0:
        return True
    else:
        return False
    

print('VERIFICADOR DE ANO BISSEXTO')
x = int(input('Digite o ano: '))
print(bissexto(x))