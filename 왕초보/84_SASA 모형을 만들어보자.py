s, a = map(int, input().split())
if(s != 1 or a != 1):
    print(min(s, a) // 2)
else:
    print(0)