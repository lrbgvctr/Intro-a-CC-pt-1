def maior_primo(num):
  def naoprimo(n):
    i = 2
    np = False
    while not np and i < n:
      if n % i == 0:
        np = True
      else:
        np = False
      i = i + 1
    return(np)
  while naoprimo(num):
    num = num - 1
  return(num)
    