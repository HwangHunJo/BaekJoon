import sys
n = int(input())
a = [0] * (10001)
for i in range(n):
    k = int(sys.stdin.readline())
    a[k] += 1

for j in range(len(a)):
    if(a[j] != 0):
        for l in range(a[j]):
            print(j)
    