from operator import itemgetter


f = open("schedule2.in")

tasks = [[int(z) for z in f.readline().split()]
         for i in range(int(f.readline()))]

tasks.sort(key=itemgetter(1), reverse=True)

used = {}

for d, c in tasks:
    for day in range(d, 0, -1):
        if day in used:
            continue
        used[day] = c
        break

total = sum(used.values())
print(total)
