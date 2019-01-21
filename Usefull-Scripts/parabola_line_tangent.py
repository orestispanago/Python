import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 10
c = 0
x = np.linspace(-10, 10,num=100)
# line = -(b*x+c)



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# # Move left y-axis and bottim x-axis to centre, passing through (0,0)
# ax.spines['left'].set_position('zero')
#
# ax.spines['bottom'].set_position('zero')
# # Eliminate upper and right axes
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# # Show ticks in the left and lower axes only
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')


quad = np.poly1d([a, b, c])
line = -np.poly1d([b,c]) # y=-b*x+c
parabola = np.poly1d([a,0,0]) # y=x**2
x1,x2 = quad.r
y1,y2 = np.polyval(parabola,[x1,x2])
dpdx = np.polyder(parabola)
d = dpdx[1]
def tanline(f,x0):
    x = np.linspace(-10,10,200)
    der = dpdx(x0)*(x-x0)+np.polyval(f,x0)
    plt.plot(x,der,'k')
def ray():
    x = np.linspace(-10,10,200)
    plt.plot(x,line(x),'r')


der = tanline(parabola,x2)
ray()

plt.plot(x,parabola(x))

plt.scatter([x1,x2],[y1,y2],color='r')
plt.show()
