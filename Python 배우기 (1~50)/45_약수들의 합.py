perfect = {6 : "1 + 2 + 3",
            28 : "1 + 2 + 4 + 7 + 14",
            496 : "1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248",
            8128 : "1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064"
}

while True:
    num = int(input())
    if(num == -1):
        break
    if num in perfect:
        print(num, "=", perfect[num])
    else:
        print(num, "is NOT perfect.")