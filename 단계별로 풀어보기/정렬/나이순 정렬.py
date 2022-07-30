import sys

N = int(sys.stdin.readline())

p = []
for i in range(N):
    a = sys.stdin.readline().split()
    p.append([int(a[0]), i, a[1]])
    
p.sort()

for person in p:
    print(person[0], person[2])