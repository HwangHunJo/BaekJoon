import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((b, a))

arr.sort()


for i in range(n):
    print(arr[i][1], arr[i][0])