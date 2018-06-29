x = "Hello World!"
print(x)
n = 3.14
print(f"Ceci est le nombre pi :{n}")

def add(i,j):
    return i+j

x = add(3,2)
print(x)

i = 0
while i < 10:
    print(i)
    i+=1

for i in range(10):
    if i % 2 == 0:
        print(i)

def isPrime(n):
    res = True
    if n < 2:
        res = False
    else:
        for i in range(2,n):
            if n%i == 0:
                res = False
    return res

print(isPrime(7))
print(isPrime(8))

l = [1,2,3,4,5,6,7,8,9]
#l = range(1,10)
i = 3
x = l[i]
l.append(99)
l.remove(99)
for i in l:
    print(i)

print(sum(l,10))
print(min(l,10))
print(max(l,10))

#sum

def sum(list, n):
    if n==0:
        return 0;
    return list[n] + [sum(list, n-1)]

#min

def min(list, n):
    if n==0:
        return list[n]
    else:
        min = list[n]
        if min > list[n-1]:
            min = list[n-1]
            min(list, n-1)
        return min


#max

def max(list, n):
    if n==0:
        return list[n]
    else:
        max = list[n]
        if max < list[n-1]:
            max = list[n-1]
            max(list, n-1)
        return max

#average

def ave(list, n):
    if n==0:
        return list[n]
    else:
        return sum(list, n)/n

#getPrimeNumbers

def primeNumbers(list):
    index = 0
    primeList = []
    for i in list:
        if isPrime(list[i]):
            primeList[index] = list[i]
            index = index+1

#inverse

def invertList(list):
    for i in list, -1:
        temp = list[i]
        del list[i]
        list.add(temp)
