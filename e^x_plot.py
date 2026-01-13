import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(3 , -3, 100)
y = np.exp(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('e^x')
plt.grid()
plt.legend()
plt.show()
