sa = 0
sb = 0
for i in range(3, 0, -1):
    n = int(input())
    sa = sa + i * n
for i in range(3, 0, -1):
    n = int(input())
    sb = sb + i * n
if(sa > sb):
    print("A")
elif(sa < sb):
    print("B")
else:
    print("T")
