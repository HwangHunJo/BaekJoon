a = input()
c = 0
for i in range(3):
    if(a[i] == '5'):
        c += 1
if(c == 3):
    print("YES")
else:
    print("NO")