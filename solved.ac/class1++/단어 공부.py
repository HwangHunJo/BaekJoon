a = input().lower()
wo_list = list(set(a))
x = []

for i in wo_list:
    count = a.count(i)
    x.append(count)

if(x.count(max(x)) >= 2):
    print("?")
else:
    print(wo_list[x.index(max(x))].upper())