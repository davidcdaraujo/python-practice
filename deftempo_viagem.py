def tempo(d, v):

    return (d / v) / 60


dis = float(input("Distância: "))
vel = float(input("Velocidade média: "))
print(f"Tempo estimado: {tempo(dis, vel)}min")