def primo(m):
  i = 2
  if m == 2:
    prime = True
  else:
    prime = False
  while i < m:
    if m % i == 0:
      prime = False
      i = m + 1
    else:
      prime = True
      i = i + 1
  return (prime)


def n_primos(n):
  k = 2
  primos = 0
  while k <= n:
    if primo(k):
      primos = primos + 1
    k = k + 1
  print(primos)
