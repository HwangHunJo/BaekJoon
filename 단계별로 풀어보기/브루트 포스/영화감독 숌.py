import sys

N = int(sys.stdin.readline())
cnt = 0
i = 0

while(True):
    if cnt == N:
        break
    while(True):
        i += 1
        if '666' in str(i):
            cnt += 1
            dnum = i
            break

print(dnum)