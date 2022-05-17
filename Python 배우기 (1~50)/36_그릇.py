a = input()
sum = 0

for i in range(1, len(a)):
    if(a[i - 1] != a[i]):
        sum += 10
    else:
        sum += 5

print(sum + 10)