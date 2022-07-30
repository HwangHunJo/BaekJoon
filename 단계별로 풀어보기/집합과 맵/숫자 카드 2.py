from bisect import bisect_left, bisect_right
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    left = bisect_left(a, b[i])
    right = bisect_right(a, b[i])
    print(right - left, end=' ')