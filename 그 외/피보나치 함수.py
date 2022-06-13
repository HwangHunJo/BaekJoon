sum = [0]*2
def fibo(n):
    global sum
    if n == 0:
        return 0
        sum[0] += 1
    elif n == 1:
        sum[1] += 1
        return 1
        
    else:
        return fibo(n - 1) + fibo(n - 2)

for _ in range(int(input())):
    fibo(int(input()))
    print(sum[0], sum[1])