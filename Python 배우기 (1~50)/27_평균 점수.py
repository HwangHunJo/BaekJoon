sum = 0
for i in range(5):
    a = int(input())
    if(a < 40):
        a = 40
    sum += a

ave = int(sum / 5)

print(ave)

