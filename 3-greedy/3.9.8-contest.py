f = open('contest.in')


def readints():
    return [int(z) for z in f.readline().split()]


n, t = readints()
tasks = readints()

tasks.sort()

finish = 0
fine = 0
count = 0
for task in tasks:
    finish += task
    if finish > t:
        break
    count += 1
    fine += finish

print(count)
print(fine)
