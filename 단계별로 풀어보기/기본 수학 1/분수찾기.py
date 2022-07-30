import sys

num = int(sys.stdin.readline())

line = 1
sum = 0

while(True):
    if num <= line + sum:
        if line % 2 == 0:
            print(f"{num - sum}/{(line - (num - sum - 1))}")
            break
        else:
            print(f"{(line - (num - sum - 1))}/{(num - sum)}")
            break
    else:
        sum += line
        line += 1
    