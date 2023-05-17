def cej(n, m): #cej:comp._escolhe_j
  if (n-m)%(m+1) == 0:
    k = 0
  else:
    k = 1
  c = ((n-m)//(m+1))+k
  x = n - c * (m+1)
  return(x)