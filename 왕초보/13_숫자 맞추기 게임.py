i = 0
while(True):
    i = i + 1
    n0 = int(input())
    if(n0 == 0):
        break
    n1 = 3 * n0
    if(n1 % 2 == 0):
        n2 = n1/2
        att = "even"
    else:
        n2 = (n1 + 1)/2
        att = "odd"
    n3 = 3 * n2
    n4 = int(n3/9)
    if(n1 % 2 == 0):
        n0 = 2 * n4
    else:
        n0 = 2*n4+1
    print("%d." %(i), att, n4)