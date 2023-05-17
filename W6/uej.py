def uej(n, m):
  i = 0
  while i == 0:
    x = int(input('Quantas peças você vai tirar? '))
    if x > m:
      print('Oops! Jogada inválida! Tente de novo.')
    else:
      i = 1
  return(x)