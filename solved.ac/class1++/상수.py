a, b = input().split()
ca = [1, 2, 3]
cb = [1, 2, 3]
for i in range(3):
    ca[i] = int(a[2-i])
    cb[i] = int(b[2-i])
m = max(ca, cb)
mn = m[0] * 100 + m[1] * 10 + m[2] * 1
print(mn)