#Exercício 2

def pg(n, a, r):
  if n == 1:
      return a
  elif n > 1:
      return r * pg(n - 1, a, r)

print(pg(3,1,5))