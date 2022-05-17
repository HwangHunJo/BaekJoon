n = int(input())
sc = list(map(int, input().split()))
m = max(sc)
sum = 0
for i in range(n):
    sc[i] = sc[i]/ m * 100
    sum += sc[i]
print(sum / n)