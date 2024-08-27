altm = []
altf = []

for i in range(10):

    x = input("[f]eminino ou [m]asculino: ")
    x.lower()

    if x == "f":
        f = float(input("Digite a altura: "))
        altf.append(f)

    elif x == "m":
        m = float(input("Digite a altura: "))
        altm.append(m)

print(f"Alturas femininas: {altf}")
print(f"Alturas masculinas: {altm}")
y = altm + altf
print(f"Menor altura: {min(y)}")
print(f"Maior altura: {max(y)}")
print(f"Média entre as mulheres: {(sum(altf)) / len(altf)}")
print(f"Total de homens: {len(altm)}")