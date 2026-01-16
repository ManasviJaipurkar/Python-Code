import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2, 2, 100)
y = np.exp(x**2)
plt.figure(figsize=(5,5))
plt.plot(x,y, color = 'red')
plt.show()
