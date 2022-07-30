a = int(input())
num = 1
cnt = 0
if(a == 1):
    print(1)
else:
    for i in range(a):
        num += 6 * i
        cnt += 1
        if(num >= a):
            print(cnt)
            break
