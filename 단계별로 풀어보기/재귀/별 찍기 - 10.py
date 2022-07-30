import math
import sys

def star(n):
    stars = []

    if n == 1:
        stars.append("***")
        stars.append("* *")
        stars.append("***")

    else:
        r = star(n - 1)
        for i in range(len(r)):
            stars.append(r[i] * 3)
        for i in range(len(r)):
            stars.append(r[i] + ' '*(3 ** (n - 1)) + r[i])
        for i in range(len(r)):
            stars.append(r[i] * 3)

    return stars
n = int(sys.stdin.readline())

# print(math.ceil(math.log(n, 3)))

s = star(math.ceil(math.log(n, 3)))

for i in s:
    print(i)