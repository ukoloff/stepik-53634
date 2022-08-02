f = open("ice2.in")

names = [f.readline().strip() for i in range(int(f.readline()))]

count = 1
seen = set()
for name in names:
    if name not in seen:
        seen.add(name)
        continue
    count += 1
    seen.clear()

print(count)
