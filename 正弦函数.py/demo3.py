import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-2*np.pi,2*np.pi,0.01)
y=np.sin(x)
plt.plot(x,y)
ax = plt.gca()
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.xticks([-np.pi*2,-np.pi*3/2,-np.pi, -np.pi/2, 0, np.pi/2, np.pi,np.pi*3/2,np.pi*2],
[r'$-2\pi$',r'$-\frac{3}{2} \pi$',r'$-\pi$',r'$-\frac{1}{2}\pi$', r'0', r'$\frac{1}{2}\pi$','$\pi$',r'$\frac{3}{2}\pi$',r'$2 \pi$'])
plt.show()