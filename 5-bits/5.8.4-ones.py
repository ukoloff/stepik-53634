f = open("ones.in")

f.readline()
numbers = [int(z) for z in f.readline().split()]

def bits(n):
  count = 0
  while n != 0:
    if n & 1:
      count += 1
    n >>= 1
  return count

print(*(bits(n) for n in numbers))
