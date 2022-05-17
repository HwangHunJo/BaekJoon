n = int(input())
for i in range(n):
    a = input()
    v = c = 0
    for j in range(len(a)):
        if(a[j] == 'A' or a[j] == 'E' or a[j] == 'I' or a[j] == 'O' or a[j] == 'U' or a[j] == 'a' or a[j] == 'e' or a[j] == 'i' or a[j] == 'o' or a[j] == 'u'):
            v += 1
        else:
            if(a[j] != ' '):
                c += 1
    print(c, v)
