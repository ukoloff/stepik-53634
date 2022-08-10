f = open('time0.in')

todos = [[int(z) for z in f.readline().split()]
         for i in range(int(f.readline()))]

print(todos)
