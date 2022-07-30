n = int(input())
a = []
for _ in range(n):
    a.append(input())
a = set(a)
a = sorted(a)
a = sorted(a, key=len)
for i in a:
    print(i)
