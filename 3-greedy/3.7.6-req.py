from operator import itemgetter


f = open("request2.in")

reqs = [[int(z) for z in f.readline().split()]
        for i in range(int(f.readline()))]

reqs.sort(key=itemgetter(1))

last = 0
count = 0
for l, r in reqs:
    if l < last:
        continue
    count += 1
    last = r

print(count)
