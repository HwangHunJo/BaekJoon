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

    for i in range(a + 1, b + 1):
        if chk[i] != 1:
            prime.append(i)
    
    return prime


while(True):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    p = getprime(n, n*2)
    
    print(len(p))
