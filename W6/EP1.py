def computador_escolhe_jogada(n, m):
  if (n-m)%(m+1) == 0:
    k = 0
  else:
    k = 1
  c = ((n-m)//(m+1))+k
  x = n - c * (m+1)
  return(x)
def usuario_escolhe_jogada(n, m):
  i = 0
  while i == 0:
    x = int(input('Quantas peças você vai tirar? '))
    if x > m:
      print('Oops! Jogada inválida! Tente de novo.')
    else:
      i = 1
  return(x)
def partida():
  ultimo = 'pc'
  p0 = int(input('Quantas peças? '))
  pmax = int(input('Quantas peças podem ser retiradas? '))
  if computador_escolhe_jogada(p0, pmax) == 0:
      print('Jogador começa!')
      x = usuario_escolhe_jogada(p0, pmax)
  else:
      print('PC começa!')
      x = computador_escolhe_jogada(p0, pmax)
  p0 = p0 - x
  print(p0, 'peças restantes,', x, 'retiradas')
  while p0 > 0:
    if computador_escolhe_jogada(p0, pmax) == 0:
      print('vez do jogador!')
      x = usuario_escolhe_jogada(p0, pmax)
      ultimo = 'user'
    else:
      print('vez do PC.')
      x = computador_escolhe_jogada(p0, pmax)
      ultimo = 'pc'
    p0 = p0 - x
    print(p0, 'peças restantes,', x, 'retiradas')
  print('O vencedor é o', ultimo)
  return(ultimo)
print('Olá! Que os jogos comecem e a sorte esteja sempre do seu lado!')
tipo = int(input('Digite "1" se deseja jogar um campeonado e "2" se prefere uma partida individual: '))
if tipo == 1:
  print('Você escolheu o campeonato.')
  part = 1
  scorepc = 0
  scoreuser = 0
  while part <= 3:
    print('Partida', part)
    ultimo=partida()
    part = part + 1
    if ultimo == 'pc':
      scorepc = scorepc + 1
    elif ultimo == 'user':
      scoreuser = scoreuser + 1
  print('Placar: Você',scoreuser,'X',scorepc,'Computador')
else:   
  print('Você escolheu uma partida.')
  partida()