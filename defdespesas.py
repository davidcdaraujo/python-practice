def dividir(conta, pessoas):

    return conta / pessoas


total = float(input("Total da conta: "))
pes = int(input("Pessoas: "))
print(f"Cada pessoa irá pagar: {dividir(total, pes)}")