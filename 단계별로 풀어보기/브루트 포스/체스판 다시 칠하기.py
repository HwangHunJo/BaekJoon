N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(input())

cnt = []

for i in range(N - 7):
    for j in range(M - 7):
        b_board = 0
        w_board = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != "W":
                        w_board += 1
                    if board[k][l] != "B":
                        b_board += 1
                else:
                    if board[k][l] != "B":
                        w_board += 1
                    if board[k][l] != "W":
                        b_board += 1
        cnt.append(min(w_board, b_board))
print(min(cnt))