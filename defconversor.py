def converter(real, dolar):

    return real * dolar


x = float(input("Dinheiro em real: "))
y = float(input("Cotação do dólar: "))
print(f"Total convertido: R${converter(x, y)}")