a = int(input())
b = int(input())
c = list(map(int, input().split()))
c = sorted(c, reverse=True)
res = 0
for i in range(b):
    if(a <= 1):
        break
    while(True):
        if(a < int(c[i])):
            break
        res = res + a / int(c[i])
        a = a / int(c[i])
print(res)