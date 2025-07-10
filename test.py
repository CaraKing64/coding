import random


def h(x):
  if x > 0 and x < 2:
    return 0.1
  elif x > 2 and x < 5:
    return 0.2
  elif x > 5 and x < 7:
    return ((-0.1 * x) + 0.7)
  

n = 100

average = 0

for i in range(1, n):
  x = random.random()*7
  print(x, h(x))
  average += h(x)

print(average/n)