#다시 복습#
t = int(input())

for i in range(t):
    cnt, word = input().split()
    for x in word:
        print(x * int(cnt), end = '')
    print()