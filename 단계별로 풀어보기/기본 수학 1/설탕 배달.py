import sys

n = int(sys.stdin.readline())
cnt = 0

while(True):
    if n % 5 == 0:
        n -= 5
        cnt += 1
    elif n % 3 == 0:
        n -= 3
        cnt += 1
    elif n >= 5:
        n -= 5
        cnt += 1
    else:
        break
    if n <= 2:
        break
if n == 0:
    print(cnt)
else:
    print(-1)
