a, b, c = map(int, input().split())

if(a < b):
    tmp = a
    a = b
    b = tmp
if(a < c):
    tmp = c
    c = a
    a = tmp
if(b < c):
    tmp = c
    c = b
    b = tmp
print(b)