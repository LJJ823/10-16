import numpy as np
import matplotlib.pyplot as plt

a=1

plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

x = np.arange(-3, 3, 0.1)
y1 = pow(2,a*x)
y2 = pow(2,-a*x)
y3 = pow(2,0*x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()