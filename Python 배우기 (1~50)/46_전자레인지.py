a = int(input())
m5 = m1 = s10 = 0
p = True
while(True):
    if(a % 10 != 0):
        print(-1)
        p = False
        break
    elif(a >= 300):
        m5 += 1
        a -= 300
    elif(a >= 60):
        m1 += 1
        a -= 60
    elif(a >= 10):
        s10 += 1
        a -= 10
    else:
        break
if(p != False):
    print(m5, m1, s10)
