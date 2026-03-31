#fibo
primero=1
segundo=2
aux=0
suma=2
while True:
    aux=primero+segundo
    primero=segundo
    segundo=aux
    if segundo<4_000_000 and segundo%2==0:
        suma=suma+aux
    if segundo>4_000_000:
        break
print(f"Suma: {suma}")