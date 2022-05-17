n = int(input())

for i in range(n):
    y = k = 0
    for j in range(9):
        n1, n2 = map(int, input().split())
        y += n1
        k += n2
    if(y > k):
        print("Yonsei")
    elif(y < k):
        print("Korea")
    else:
        print("Draw")