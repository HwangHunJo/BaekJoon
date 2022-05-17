n = int(input())
a = input()
e = n2 = 0
for i in range(n):
    if(a[i] == 'e'):
        e += 1
    elif(a[i] == '2'):
        n2 += 1

if(e > n2):
    print("e")
elif(e < n2):
    print(2)
else:
    print("yee")