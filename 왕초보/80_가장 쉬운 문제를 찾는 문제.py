n = int(input())
min = 4
min_loc = 0
k = []
for i in range(n):
    t, l = map(str, input().split())
    k.append(t)
    l = int(l)
    if(min > l):
        min = l
        min_loc = i
print(k[min_loc]) 
