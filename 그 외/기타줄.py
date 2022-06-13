n, m = map(int, input().split())
min_pack = 1000
min_piece = 1000
sum = 0
for i in range(m):
    a, b = map(int, input().split())
    if min_pack > a:
        min_pack = a
    if min_piece > b:
        min_piece = b

while(n > 0):
    if(min_pack <= n * min_piece):
        sum += min_pack
        n -= 6
    elif(min_pack > n * min_piece):
        sum += n * min_piece
        n -= n

print(sum)