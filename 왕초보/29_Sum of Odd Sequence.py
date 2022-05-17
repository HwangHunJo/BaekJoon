n = int(input())
for i in range(n):
    sum = 0
    k = int(input())
    for j in range(1, k+1):
        if(j % 2 != 0):
            sum += j
    print(sum)