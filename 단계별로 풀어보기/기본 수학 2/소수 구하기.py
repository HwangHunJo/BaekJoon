import sys

def getprime(a, b):
    chk = [0] * (b + 1) 
    chk[0] = 1
    chk[1] = 1

    prime = []
    for i in range(2, b + 1):
        for j in range(i * 2, b + 1, i):
            if chk[j] != 1:
                chk[j] = 1

    for i in range(a, b + 1):
        if chk[i] != 1:
            prime.append(i)
    
    return prime


n, m = map(int, sys.stdin.readline().split())
p = getprime(n, m)

for i in p:
    print(i)
