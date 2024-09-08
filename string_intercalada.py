def intercalar(x, y):
    res = []
    tam1 = len(x)
    tam2 = len(y)
    i = 0

    while i < tam1 and i < tam2:
        res.append(x[i])
        res.append(y[i])
        i += 1
    while i < tam1:
        res.append(x[i])
        i += 1
    while i < tam2:
        res.append(y[i])
        i += 1
    return ''.join(res)


str1 = "abc"
str2 = "defg"
print(f"String 1: {str1}")
print(f"String 2: {str2}")
print(f"Intercaladas: {intercalar(str1, str2)}")