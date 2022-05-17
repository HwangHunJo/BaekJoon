v = int(input())
a = b = 0
vot = input()
for i in range(v):
    if(vot[i] == 'A'):
        a += 1
    elif(vot[i] == 'B'):
        b += 1

if(a > b):
    print("A")
elif(a < b):
    print("B")
else:
    print("Tie")
