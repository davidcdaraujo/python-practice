def total(conta):

    g = conta * 0.10
    return g + conta


x = float(input("Conta: "))
print(f"Com gorjeta: {total(x)}")