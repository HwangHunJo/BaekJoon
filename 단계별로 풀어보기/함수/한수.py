import sys

def han(x):
    cnt = 0
    
    for i in range(1, x + 1):
        if i < 100:
            cnt += 1
        else:
            a = i // 100
            b = (i % 100) // 10
            c = (i % 100) % 10
            if b - a == c - b:
                cnt += 1
    return cnt

x = int(sys.stdin.readline())
print(han(x))


