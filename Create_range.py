#Create Range
# range(start, stop, step)

x = range(8)
x
print(list(x))

y = range(1, 10, 2)
print(list(y))

z = range(0, 10, 2)
print(list(z))

a = range(-2, 2, 100)
print(list(a))

import numpy as np
x = np.linspace(-2, 2, 10)
print(x)

for i in range(10):
  print(i)