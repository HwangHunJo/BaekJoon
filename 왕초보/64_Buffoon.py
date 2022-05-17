n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

if(a[0] >= max(a)):
    print('S')
else:
    print('N')