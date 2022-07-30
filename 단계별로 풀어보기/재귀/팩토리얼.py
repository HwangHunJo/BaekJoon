def fac(n):
  if(n == 1 or n == 0):
    return 1
  else:
    return fac(n - 1) * n

a = int(input())
print(fac(a))