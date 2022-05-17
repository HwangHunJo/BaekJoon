a = [False]
for _ in range(1, 10001):
    a.append(False)

def D(n):
    dn = n
    while(n > 0):
        dn += n % 10
        n //= 10
    return dn

for i in range(1, 10001):
    num = D(i)
    if(num <= 10000):
        a[num] = True

for j in range(1, 10001):
    if(a[j] == False):
        print(j)