
n=2_000_000
L=[]
suma=0
for i in range(2,n+1):
    primo=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            primo=0
            break
    if primo:
        suma=suma+i
suma