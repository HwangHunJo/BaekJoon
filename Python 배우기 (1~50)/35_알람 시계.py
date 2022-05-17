h, m = map(int, input().split())

if(m >= 45):
    m -= 45
else:
    h -= 1
    m += 60
    m -= 45
if(h < 0):
    h = h + 24

print(h, m)