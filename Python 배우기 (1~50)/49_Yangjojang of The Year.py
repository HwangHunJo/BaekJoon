n1 = int(input())
for i in range(n1):
    n2 = int(input())
    un = [None] * n2
    us = [None] * n2
    for j in range(n2):
        un[j], us[j] = input().split()
        us[j] = int(us[j])
    print(un[us.index(max(us))])
