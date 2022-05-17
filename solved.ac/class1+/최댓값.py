max = 0
a = []
for i in range(9):
    a.append(input())
    if(int(a[i]) > max):
        max = int(a[i])
        max_loc = i+1
print(max)
print(max_loc)