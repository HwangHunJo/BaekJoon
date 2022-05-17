n = int(input())
for i in range(n):
    n, o = map(str, input().split())
    n = int(n)
    for j in range(n):
        print(o, end = '')
    print()