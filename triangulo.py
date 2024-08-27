x = float(input("Lado 1: "))
y = float(input("Lado 2: "))
z = float(input("Lado 3: "))

if x + y > z and x + z > y and y + z > x:
    a = x + y + z
    print(f"Perímetro: {a}")

else:
    print("Os valores não satisfazem um triângulo.")