def pangrama(x):
    min = x.lower()
    y = 'qwertyuiopasdfghjklzxcvbnm'
    z = set(y)
    for i in z:
        if i in min:
            return(f'"{x}" é um pangrama.')
        else:
            return('"{x}" não é um pangrama.')
        

frase = 'Um pequeno jabuti xereta viu dez cegonhas felizeswy.'
print(pangrama(frase))