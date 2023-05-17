n = int(input('p0'))
m = int(input('pmax'))
x = m 
while x >= 1:
  c = (n-x)/(m+1)
  if int(c) != c:
    x = x-1
  else:
    break
print(x)
