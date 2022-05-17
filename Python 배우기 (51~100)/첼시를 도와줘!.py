price_arr = []
player = {}
for _ in range(int(input())):
    price_arr.clear()
    player.clear()
    for _ in range(int(input())):
        price, name = input().split()
        price_arr.append(int(price))
        player[price] = name
    print(player[str(max(price_arr))])
