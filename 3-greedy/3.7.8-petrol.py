f = open('petrol2.in')


def readints():
    return [int(z) for z in f.readline().split()]


n, dist, trip = readints()
stations = readints()

idx = len(stations) - 1
result = []
while dist > trip:
  found = False
  for i in range(idx, -1, -1):
    if stations[i] >= dist:
      continue
    if stations[i] < dist - trip:
      break
    idx = i
    found = True
  if not found:
    count = -1
    break
  dist = stations[idx]
  result.append(dist)
result.reverse()

print(result)
print(len(result))
