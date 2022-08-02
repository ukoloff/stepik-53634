f = open("ice.in")

names = [f.readline().strip() for i in range(int(f.readline()))]
print(*names)
