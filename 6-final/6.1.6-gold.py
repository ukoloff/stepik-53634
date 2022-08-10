f = open('gold3.in')

f.readline()
bars = [int(z) for z in f.readline().split()]

S = sum(bars)
UB = S // 2

sums = {0}
for bar in bars:
  sums.update([i + bar for i in sums if i + bar <= UB])

delta = S - 2 * max(sums)
print(delta)
