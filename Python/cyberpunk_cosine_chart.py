#%%
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm
import mplcyberpunk

t = np.arange(0, 6.4, 0.1) #time
f = 1 #frequency
amplitudes = np.arange(-10,11, 1)
A = [x * np.cos(f*t) for x in amplitudes] #amplitude

colormap_sect = np.linspace(0, 1, len(amplitudes))
colors = [cm.cool(x) for x in colormap_sect]

plt.rcParams['figure.figsize'] = [6, 4]
plt.style.use("cyberpunk")
plt.xlim(right=6.3)

for i in range(len(A)):
    plt.plot(t, A[i], color=colors[i])

mplcyberpunk.make_lines_glow()
plt.show()
