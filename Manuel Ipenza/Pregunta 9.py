for i in range(1000):
    for j in range(1000):
        k=1000-i-j
        if i<j<k and (i**2+j**2 == k**2):
            print(i*j*k)