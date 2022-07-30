import sys

n = sys.stdin.readline().split()[0]
a = []

for i in n:
    a.append(i)

a.sort(reverse = True)
print("".join(a))