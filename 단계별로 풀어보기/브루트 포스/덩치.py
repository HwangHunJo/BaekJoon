import sys

N = int(sys.stdin.readline())

rank = [1] * N
p = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    p.append([x, y])

for i in range(len(p)):
    for j in range(len(p)):
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            rank[i] += 1

for i in rank:
    print(i, end = ' ')