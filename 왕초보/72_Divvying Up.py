n = int(input())
sum = 0
a = []
while(True):
    if(len(a) == n):
        break
    a = list(map(int, input().split()))

for i in range(n):
    sum += a[i]
if(sum % 3 == 0):
    print("yes")
else:
    print("no")
