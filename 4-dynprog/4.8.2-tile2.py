def tile2(n):
  a, b = 1, 1
  for i in range(n):
    a, b = b, a + b
  return a

print(tile2(42) % 100)
print(tile2(100000) % 1000000000)
