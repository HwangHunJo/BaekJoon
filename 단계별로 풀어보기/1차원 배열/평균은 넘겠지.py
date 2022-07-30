n = int(input())
for i in range(n):
    sum = 0
    cnt = 0
    a = list(map(int, input().split()))
    l = a[0]
    a.pop(0)

    for k in a:
        sum += k
    ave = sum / l

    for j in range(l):
        if(a[j] > ave):
            cnt += 1
            
    ave = (cnt/l) * 100
    print("%.3f%%"%(ave))