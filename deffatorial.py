def fatorial(num):
    
    fat = 1

    for i in range(num):
        i += 1
        fat *= i
    
    return fat


n = int(input("Número: "))
print(f"Fatorial de {n} = {fatorial(n)}")