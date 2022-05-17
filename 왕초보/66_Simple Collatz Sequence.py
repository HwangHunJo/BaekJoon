# a = int(input())
# i = 0
# while(True):
#     if(a == 1):
#         break
#     i += 1
#     if(a % 2 == 0):
#         a /= 2
#     else:
#         a += 1
# print(i)
i = 0
def re(a):
    global i
    if(a == 1):
        return i
    i += 1
    if(a % 2 == 0):
        a //= 2
        re(a)
    else:
        a += 1
        re(a)
re(int(input()))
print(i)