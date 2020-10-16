import numpy as np
import matplotlib.pyplot as plt
def unit(t):
     r=np.where(t>-1.0,2.5,0.0)
     return r
t=np.linspace(-3.0,5.0,1000)
plt.ylim(-1.0,3.0)
plt.plot(t,unit(t))
plt.show()