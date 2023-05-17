l = []
a = 1
while a != 0:
  a = int(input('Digite um numero: '))
  l.append(a)
l.pop(-1)
while len(l) > 0:
  print(l.pop(-1))
  