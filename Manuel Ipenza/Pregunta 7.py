c=0
n=1
while True:
    n=n+1
    primo=1
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            primo=0
            break
    
    if primo:
        c=c+1
        if c==10001:
            print(n)
            break