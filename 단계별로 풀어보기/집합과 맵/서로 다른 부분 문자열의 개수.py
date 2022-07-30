import sys

s = sys.stdin.readline().split("\n")[0]

per = []
for i in range(0, len(s)):
    for j in range(0, len(s) - i):
        per.append(s[j:i+j+1])
print(len(set(per)))