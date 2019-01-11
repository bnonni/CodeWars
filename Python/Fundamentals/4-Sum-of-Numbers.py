def get_sum(a,b):
  lower = a if a < b else b
  upper = b if b > a else a
  if a != b and a > 0:
    for num in range(lower, upper):
      inc = lower+1
      total = lower + inc
    return total
  else:
    return a or b

print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))
"""
(-1, 2)

lower = a = -1
upper = b = 2

plusup = 3

for num in range(-1, 3)
  inc = lower+1
  lower = -1 + 1 = 0
  lower+=inc
  /////
  inc = -1 + 1 = 0
  lower = -1 + 0

"""
