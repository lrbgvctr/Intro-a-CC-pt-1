def baskara(a, b, c):
  d = b**2 - (4 * a * c)
  if d >= 0:
    import math
    sd = math.sqrt(d)
    r1 = (sd - b)/(2 * a)
    r2 = (-b - sd)/(2 * a)
    if r1 == r2:
      print(r1)
    else:
      print(r1, r2)