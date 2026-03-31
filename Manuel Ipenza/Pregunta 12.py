def factores(n):
    c=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            c=c+2
        if i == n**0.5:
            c = c-1
    return c
div=500
triangulo = 1
i=1
while True:
    if factores(triangulo) > div:
        print(triangulo)
        print("yasta")
        break
    i+=1
    triangulo+=i