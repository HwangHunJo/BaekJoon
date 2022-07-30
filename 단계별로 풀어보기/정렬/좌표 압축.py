import sys

N = int(sys.stdin.readline())

x = list(map(int, sys.stdin.readline().split()))

f = sorted(list(set(x)))
dic = {f[i] : i for i in range(len(f))}

for i in x:
    print(dic[i], end = ' ')

