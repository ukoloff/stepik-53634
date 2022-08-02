f = open('cont2.in')


def readints():
    return [int(z) for z in f.readline().split()]


n, W = readints()
items = [readints() for i in range(n)]

value = 0

items.sort(key=lambda z: z[1] / z[0], reverse=True)
for w, c in items:
    if W <= 0:
        break
    ratio = min(1, W / w)
    value +=  ratio * c
    W -= ratio * w

print(value)
