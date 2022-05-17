n = int(input())
a, b, c, d, e = map(int, input().split())
cnt = 0

if(a == n):
    cnt += 1
if(b == n):
    cnt += 1
if(c == n):
    cnt += 1
if(d == n):
    cnt += 1
if(e == n):
    cnt += 1

print(cnt)