l = int(input('Digite a largura: ')) - 2
h = int(input('Digite a altura: ')) - 2
i = 0
j = 0
while i < (l + 2):
  print('_', end='')
  i = i + 1
i = 0
print('')
while i < h:
  print('|', end='')
  while j < l:
    print(' ', end='')
    j = j + 1
  print('|', end='')
  print()
  j = 0
  i = i + 1
i = 0
while i < (l + 2):
  print('_', end='')
  i = i + 1