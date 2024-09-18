def anagrama(x, y):
    a = x.lower()
    b = y.lower()
    str1 = sorted(a)
    str2 = sorted(b)
    if str1 == str2:
        print('As strings são anagrams')
    else:
        print('As strings não são anagrmas')


anagrama('america', 'iracema')