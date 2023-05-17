n = input('Digite o valor de n: ')
tamanho = len(n)
num = int(n)
i = 0
soma = 0
while i < tamanho:
  soma = soma+(num % 10)
  num = num // 10
  i = i + 1
print(soma)