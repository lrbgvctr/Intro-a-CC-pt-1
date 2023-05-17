type = int(input('Se a temperatura for ambiente, digite 1, se for corporal, digite 2: '))
Fint = input('F= ')
F = float(Fint)
Cfloat = (F - 32) * 5 / 9
if type == 1:
  C = int(Cfloat)
  if C < 20:
    print('Está frio!')
  elif C > 30:
    print('Está calor!')
  else:
    print('Está ameno:')
else:
  C = float("%.1f" % Cfloat)
  
  if C >= 37:
    print('você está com febre!')
  elif C < 35:
    print('você está hipotermico:')
  else:
    print('está tudo bem')
print('C=', C)
