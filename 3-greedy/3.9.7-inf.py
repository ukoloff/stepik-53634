f = open("request2.in")

reqs = [[int(z) for z in f.readline().split()]
        for i in range(int(f.readline()))]

points = []
for l, r in reqs:
  points.append((l, +1))
  points.append((r, -1))

points.sort()

count = 0
usage = 0
for time, delta in points:
  usage += delta
  count = max(count, usage)

print(count)
