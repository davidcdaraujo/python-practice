def verificar(texto, x, y):
    if x + y == texto:
        return(f'"{y}" é subsequênte à "{x}".')
    else:
        return('Não são subsequêntes.')


text = 'Em dias de Sol recomenda-se utilizar protetor solar.'
a = 'Em dias de Sol '
b = 'recomenda-se utilizar protetor solar.'
print(f'texto: "{text}"\na: "{a}"\nb: "{b}"')
print(verificar(text, a, b))