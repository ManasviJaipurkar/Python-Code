import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.exp(-x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, color = 'red')
plt.title('Inverse Exponential Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
