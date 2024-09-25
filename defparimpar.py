def paridade(n):

    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


num = int(input("Número: "))
print(paridade(num))