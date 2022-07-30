ran = int(input())
for i in range(ran):
    H, W, N = map(int, input().split())
    room = []
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            room.append(i + j*100)
    print(room[N - 1])
