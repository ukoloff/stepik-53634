def brackets(n):

  def rec(head='', bal=0):
    if len(head) == 2 * n:
      yield head
    if 2 * n - len(head) > bal:
      yield from rec(head + '(', bal + 1)
    if bal > 0:
      yield from rec(head + ')', bal - 1)

  yield from rec()

print(*brackets(3), sep='\n')
print('-' * 80)

from itertools import islice

N = 8644
print(*islice(brackets(10), N-1, N))
