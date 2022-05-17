a, b = map(int, input().split())
if(a > b):
    tmp = b
    b = a
    a = tmp
if(a == b):
    print(0)
else:
    print(b - (a + 1) )

for i in range(a + 1, b):
    if(i == b - 1):
        print(i)
    else:
        print(i, end = ' ')

