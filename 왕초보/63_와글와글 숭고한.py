s, k, h = map(int, input().split())
m = min(s, k, h)
if(s + k + h >= 100):
    print("OK")
elif(m == s):
    print("Soongsil")
elif(m == k):
    print("Korea")
elif(m == h):
    print("Hanyang")