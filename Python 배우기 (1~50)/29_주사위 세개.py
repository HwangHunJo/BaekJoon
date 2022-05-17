from genericpath import samefile


a, b, c = map(int, input().split())

max = 0
if(max < a):
    max = a
if(max < b):
    max = b
if(max < c):
    max = c
same = 1

if(a == b == c):
    print(10000+a*1000)
elif(a == b != c or a == c != b):
    print(1000+a*100)
elif(a != b == c or a == b != c):
    print(1000+b*100)
else:
    print(max*100)
