def brackets(n):
  stack = []

  def rec(head=''):
    if len(head) == 2 * n:
      yield head
      return
    for bra, ket in ('()', '[]'):
      if len(head) + len(stack) < 2 * n:
        stack.append(bra)
        yield from rec(head + bra)
        stack.pop()
      if len(stack) > 0 and stack[-1] == bra:
        stack.pop()
        yield from rec(head + ket)
        stack.append(bra)

  yield from rec()

print(*brackets(2), sep='\n')
print('-' * 80)
from itertools import islice

N = 20
print(*islice(brackets(3), N - 1, N))

N = 8233
print(*islice(brackets(7), N - 1, N))
