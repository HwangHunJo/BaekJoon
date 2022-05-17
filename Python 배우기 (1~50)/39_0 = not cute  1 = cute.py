n = int(input())
c1 = c2 = 0
for i in range(n):
    a = int(input())
    if(a == 1):
        c1 += 1
    else:
        c2 += 1

if(c1 > c2):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")