n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(input())

for _ in range(m):
    b.append(input())

inter = list(set(a) & set(b))
inter.sort()
print(len(inter))
for i in inter:
    print(i)
