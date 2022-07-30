import sys

def hanoi(a, b, n):
    if n == 1:
        print(a, b)
        return
    
    empty = 6 - (a + b)

    hanoi(a, empty, n - 1)
    print(a, b)
    hanoi(empty, b, n - 1)


n = int(sys.stdin.readline())

print(2 ** n - 1)

hanoi(1, 3, n)
