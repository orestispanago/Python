import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 1
c = 0
r = 1
x = np.linspace(-1, 1,num=100)

id_pos = x # identity line
id_neg = -x

y = a*x**2+b*x**2+c - 1.75
circle = -np.sqrt(r**2 - x**2)

plt.plot(x,y)
plt.plot(x,circle)
plt.plot(x,id_pos)
plt.plot(x,id_neg)
plt.show()
