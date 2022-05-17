n = int(input())
max_res = 0

for i in range(n):
    a, b, c = map(int, input().split())

    max_n = 0
    if(max_n < a):
        max_n = a
    if(max_n < b):
        max_n = b
    if(max_n < c):
        max_n = c

    if(a == b == c):
        if(max_res < 10000+a*1000):
            max_res = 10000+a*1000
    elif(a == b != c or a == c != b):
        if(max_res < 1000+a*100):
            max_res = 1000+a*100
    elif(a != b == c or a == b != c):
        if(max_res < 1000+b*100):
            max_res = 1000+b*100
    else:
        if(max_res < max_n*100):
            max_res = max_n*100

print(max_res)
