def remove_repetidos(lista):
  lista1 = sorted(lista)
  lista1.append(0)
  final = []
  for i in range(len(lista1) - 1):
    if lista1[i] != lista1[i+1]:
      final.append(lista1[i])
  return(final)
      
     