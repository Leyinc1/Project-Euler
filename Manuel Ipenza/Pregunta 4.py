def palindromo(n):
    L=[]
    for i in range(6):
        L.append(n%10)
        n=n//10
    Lo=L.copy()
    L.reverse()
    if Lo==L:
        return True
    else:
        return False
L=[]     
for i in range(100,1000):
    for j in range(100,1000):
        if palindromo(i*j):
            L.append([i,j])
mayor=0
for i in L:
    if((i[0]*i[1])>mayor):
        mayor=i[0]*i[1]
        J=[i[0],i[1]]
print(f"el mayor palindromo es: {mayor} y sus factores son: {J}")