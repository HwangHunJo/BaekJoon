import sys
n, m = map(int, sys.stdin.readline().split())
add = []
s = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
                if s[i] + s[j] + s[k] <= m:
                    add.append(s[i] + s[j] + s[k])

print(max(add))