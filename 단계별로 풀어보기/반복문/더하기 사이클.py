n1 = int(input())
a = n1
cnt = 0
newn = None
while(a != newn):
    sum = n1 // 10 + int(n1 % 10)
    newn = int((n1 % 10) * 10) + sum % 10
    n1 = newn
    cnt += 1
print(cnt)
    