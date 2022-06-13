N = int(input())
al = input()
s = []
stack = []

for i in range(N):
    s.append(int(input()))

for i in al:
    if i >= 'A' and i <= 'Z':
        stack.append(s[ord(i) - ord('A')])

    else:
        n2 = stack.pop()
        n1 = stack.pop()

        if i == '+':
            stack.append(n1 + n2)
        elif i == '-':
            stack.append(n1 - n2)
        elif i == '*':
            stack.append(n1 * n2)
        elif i == '/':
            stack.append(n1 / n2)

print("%.2f" %stack[0])