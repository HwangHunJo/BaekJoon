for l in range(int(input())):
    if(l != 0):
        print()
    n = int(input())
    i = 1

    print("Pairs for %d:" %n, end = ' ')
    for j in range((n-1)//2):
        if(j != 0):
            print(",", end = ' ')
        print(i, n - i, end = '')
        i += 1
