import sys

N, M = map(int, sys.stdin.readline().split())

S = {}


for _ in range(N):
    s = sys.stdin.readline().split()[0]
    S[s] = True

cnt = 0
for _ in range(M):
    MS = sys.stdin.readline().split()[0]
    if S.get(MS) == True:
        cnt += 1

print(cnt)
