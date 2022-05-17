n = int(input())
m = int(input())

i = 1
arr = []

while(True):
    if(i * i >= n and i * i <= m):
        arr.append(i * i)
    elif(i > m):
        break
    i += 1
sum = 0
for i in arr:
    sum += i

if(len(arr) == 0):
    print(-1)
else:
    print(sum)
    print(min(arr))
