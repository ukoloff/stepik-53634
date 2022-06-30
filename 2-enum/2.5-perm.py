def permutations(n):
  used = [0] * n
  def rec(p=()):
    if len(p) == n:
      yield p
      return
    for i in range(n):
      if used[i]:
        continue
      used[i] = 1
      yield from rec(p + (i + 1,))
      used[i] = 0
  yield from rec()

print(*permutations(3), sep='\n')
