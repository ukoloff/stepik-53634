def tiles3(n):
  if n < 3:
    return 1
  return tiles3(n-1) + tiles3(n-3)

for i in range(21):
  print(i, tiles3(i))
