h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

if(m1 > m2):
    m2 += 60
    h2 -= 1
if(s1 > s2):
    s2 += 60
    m2 -= 1

h = h2 - h1
m = m2 - m1
s = s2 - s1

if(h < 10):
    h = '0' + str(h)
if(m < 10):
    m = '0' + str(m)
if(s < 10):
    s = '0' + str(s)

a = []

a.append(str(h))
a.append(str(m))
a.append(str(s))

print(':'.join(a))
