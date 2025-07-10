import math


v1 = (1, 1, 1, 0)
v2 = (0, 2, 1, -1)
v3 = (0, 0, 0, 1)

x1 = 5 / math.sqrt(6)
u = (x1, x1, -2*x1, 0)


sum1 = 0
sum2 = 0
sum3 = 0
for i in range(len(u)):
  sum1 += u[i] * v1[i]
  sum2 += u[i] * v2[i]
  sum3 += u[i] * v3[i]

print(sum1)
print(sum2)
print(sum3)
