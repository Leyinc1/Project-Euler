n=20
encontrado=False
while not encontrado:
    contador=0
    for i in range(1,21):
        if i<=n and n%i!=0:
            contador=0
            continue
        else:
            contador=contador+1
        if contador == 20:
            encontrado=True
    if encontrado:
        print(f"Encontrado: {n}")
    else:
        n=n+20