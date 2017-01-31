# convolution.py

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from time import perf_counter

f = np.zeros(1000)
f[300:700] = 1
g = np.zeros(1000)
g[300:700] = np.arange(0,1,1/400)
t = perf_counter()
h = np.convolve(f,g)
print('NumPy: {} s'.format(perf_counter()-t))

t = perf_counter()
h = signal.fftconvolve(f,g)
print('SciPy: {} s'.format(perf_counter()-t))


fig = plt.figure(1, figsize=(20,10))
ax1 = fig.add_subplot(321)
ax1.plot(f)
ax2 = fig.add_subplot(322)
ax2.plot(g)
ax3 = fig.add_subplot(323)
ax3.plot(h)
# ax4 = fig.add_subplot(324)
# ax4.plot(i)
plt.show()
