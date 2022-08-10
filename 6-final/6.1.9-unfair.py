f = open('gold4.in')

f.readline()
bars = [int(z) for z in f.readline().split()]

bars.sort()
diff = sum(bars[len(bars)//2:]) - sum(bars[:len(bars)//2])
print(diff)
