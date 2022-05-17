n, m = map(int, input().split())
s = n*m
cutn = 0
while(1):
    if(s == 1):
        break
    s -= 1
    cutn += 1
print(cutn)