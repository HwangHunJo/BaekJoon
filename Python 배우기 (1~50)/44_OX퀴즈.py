n = int(input())
sum = 0
for i in range(n):
    a = 0
    arr = input()
    for j in range(len(arr)):
        if(arr[j] == 'O'):
            a += 1
            sum += a
        elif(arr[j] == 'X'):
            a = 0
    print(sum)
    sum = 0
