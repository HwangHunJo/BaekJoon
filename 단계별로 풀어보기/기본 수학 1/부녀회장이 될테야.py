t = int(input())
apart = []
for i in range(t):
    n = int(input())
    k = int(input())
    apart = [[0 for _ in range(14)] for _ in range(n + 1)]
    
    for j in range(14):
        apart[0][j] = j + 1

    for l in range(n + 1):
        apart[l][0] = 1
    for l in range(1, n + 1):
        for j in range(1, 14):
            apart[l][j] = apart[l][j - 1] + apart[l - 1][j]


    

    print(apart[n][k - 1])
