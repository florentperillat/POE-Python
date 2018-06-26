def primeNumbers (n):
    prime = True
    k = 0
    for i in 0,n:
        for j in 2,n[i]**1/2:
            if n[i]%j==0:
                prime=False
                break
        if prime:
            ret[k]=n[i]
            k=k+1
        prime=True
    return ret


n = [1,2,3,4,5,6,7,8,9]
print(primeNumbers(n))