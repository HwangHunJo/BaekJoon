from cmath import sqrt


import math
x1, y1, r1 = map(int, input().split())
s1 = x1 + y1 + r1
x2, y2, r2 = map(int, input().split())
d = (x1 - x2) **2 + (y1 - y2) ** 2
if(d < (r1 + r2)**2):
    print("YES")
else:
    print("NO")

#두 원의 반지름의 합이 두 원의 중심과의 거리보다 크면 겹치고, 작으면 안 겹친다.