def tiles3(n):
  a, b, c = 1, 1, 1
  for i in range(n):
    a, b, c = b, c, a + c
  return a

for i in range(21):
  print(i, tiles3(i))
