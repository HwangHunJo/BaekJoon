n = int(input())
for i in range(n):
    a = list(map(str, input().split()))
    result = float(a[0])
    for j in range(1, len(a)):
        if a[j] == '@':
            result *= 3
        elif a[j] == '%':
            result += 5
        elif a[j] == '#':
            result -= 7
    
    print("%0.2f"%result)
    