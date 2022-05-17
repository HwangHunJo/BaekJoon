a = int(input())
b = int(input())

c1 = int(b % 10) * a
print(c1)

c2 = int(b % 100 / 10) * a
print(c2)

c3 = int(b / 100) * a
print(c3)

print(c1 + c2*10 + c3*100)