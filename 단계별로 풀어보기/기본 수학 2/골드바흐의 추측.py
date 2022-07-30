import sys

def getprime(a):
    chk = [0] * (a + 1) 
    chk[0] = 1
    chk[1] = 1

    prime = []
    for i in range(2, a + 1):
        for j in range(i * 2, a + 1, i):
            if chk[j] != 1:
                chk[j] = 1

    for i in range(2, a + 1):
        if chk[i] != 1:
            prime.append(i)
    
    return prime

def gold(b):
    l1 = []
    l2 = []
    l3 = []
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i] + b[j] == n:
                l1.append(b[i])
                l2.append(b[j])
                
    for i in range(len(l1)):
        l3.append(abs(l1[i] - l2[i]))
    m = min(l3)
    print(l1[l3.index(m)], l2[l3.index(m)])
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    p = getprime(n)
    gold(p)


