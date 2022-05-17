t, m = map(int, input().split())
om = int(input())
t += om / 60
m += om % 60

if(m >= 60):
    m -= 60
    t += 1

if(t >= 24):
    t -= 24

print(int(t), int(m))