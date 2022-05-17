r, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(r):
    if(a[i] < x):
        print(a[i], end = ' ')  