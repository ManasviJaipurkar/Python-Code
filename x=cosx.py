import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100) 
print(x)
y1 = x
y2 = np.cos(x)

plt.figure(figsize=(5,5))
plt.plot(x,y1, label ='y=x', color = 'blue')
plt.plot(x,y2, label = 'Y = cosx', color = 'red')
plt.title('Plot of y = x and y = cos(x)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.legend()
plt.show()
