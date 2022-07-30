import sys

N = int(sys.stdin.readline())

m = 0

for i in range(1, N + 1):
    sum = 0
    s = str(i)
    sum += i
    for num in s:
        sum += int(num)
    
    if sum == N:
        m = i
        break
print(m)