def binomial(n, k):
  def fatorial(num):
    fator = 1
    i = 1
    while i < (num+1):
      fator = fator * i
      i = i + 1
    return(fator)
  fn = fatorial(n)
  fk = fatorial(k)
  fnk = fatorial((n-k))
  b = (fn / (fk * fnk))
  print(b)