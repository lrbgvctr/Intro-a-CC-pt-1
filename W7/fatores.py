#extra2.w7(comeback)
num = int(input("digite um número: "))
den = num
anterior = 1
multi = 1
while num > 0:
  if num == 1:
    if multi > 1:
      print('^', multi)
    num = 0
  else:
    den = den - 1
    while num % den != 0:
      den = den - 1
    if num // den != anterior:
      if multi > 1:
        print('^', multi, end='   ')
      else:
        print(end='  ')
      print(num // den, end=" ")
      multi = 1
    else:
      multi = multi + 1
    anterior = num // den
    num = den