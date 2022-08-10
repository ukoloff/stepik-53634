f = open('shops2.in')

f.readline()
points = [[int(z) for z in f.readline().split()] for i in range(2)]

# Quick-n-dirty greedy solution

minimum = sum(abs(a-b) for a, b in zip(*(sorted(lst) for lst in points)))

print(minimum)
