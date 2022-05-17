import sys


n, m = map(int, sys.stdin.readline().split())

name = {}
num = {}

cnt = 1

for _ in range(n):
    nam = sys.stdin.readline().strip()
    num[nam] = cnt
    name[cnt] = nam
    cnt += 1

for _ in range(m):
    ans = sys.stdin.readline().strip()

    try:
        print(name[int(ans)])

    except:
        print(num[ans])