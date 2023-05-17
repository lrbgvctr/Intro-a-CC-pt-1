num1 = int(float(input('Digite o primeiro número: ')))
num2 = int(float(input('Digite mais um número: ')))
num3 = int(float(input('Agora o último númeri: ')))
if num2 == (num1 + 1) and num3 == (num2+1):
  print('crescente')
else:
  print('não está em ordem crescente')