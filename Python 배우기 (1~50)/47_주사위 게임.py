s1 = s2 = 100
n = int(input())
for i in range(n):
    d1, d2 = map(int, input().split())
    if(d1 == d2):
        continue
    elif(d1 > d2):
        s2 -= d1
    else:
        s1 -= d2

print(s1)
print(s2)