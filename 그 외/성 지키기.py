board = []

n, m = map(int, input().split())
x = 0
for i in range(n):
    board.append(input())

flag = [False]*m
idx = 0

for i in board:
    if not 'X' in i:
        x += 1
        flag[idx] = True
        idx += 1



for i in range(m):
    cnt_x = 0
    for j in range(n):
        if board[j][i] == 'X' and flag[i] == False:
            cnt_x += 1

    if cnt_x == 0 and flag[i] == False:
        x += 1
print(x)