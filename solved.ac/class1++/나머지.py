sear = []
for i in range(10):
    a = int(input())
    a = a % 42
    sear.append(a)
            
sear = set(sear)
print(len(sear))