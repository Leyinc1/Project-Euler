def ite(n):
    c=0
    n_o=n
    while n>1:
        c=c+1
        if n%2==0:
            n= n/2
        else:
            n= 3*n+1
    return n_o,c
c_mayor=0
for i in range(1_000_000):
    n,c=ite(i)
    if c>c_mayor:
        c_mayor=c
        n_mayor=n
print(c_mayor,n_mayor)