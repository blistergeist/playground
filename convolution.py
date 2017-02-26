# convolution.py

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from time import perf_counter

f = np.zeros(1000)
f[300:700] = 1
g = np.zeros(1000)
g[300:700] = np.arange(0,1,1/400)

h = signal.fftconvolve(f,g)
i = signal.fftconvolve(f,g[::-1])
j = signal.fftconvolve(f,f)

fig = plt.figure(1, figsize=(20,10))
ax1 = fig.add_subplot(321)
ax1.set_title('F')
ax1.plot(f)
ax2 = fig.add_subplot(322)
ax2.set_title('G')
ax2.plot(g)
ax3 = fig.add_subplot(323)
ax3.set_title('Convolution')
ax3.plot(h)
ax4 = fig.add_subplot(324)
ax4.set_title('Cross-Correlation')
ax4.plot(i)
ax5 = fig.add_subplot(325)
ax5.set_title('Autocorrelation')
ax5.plot(j)
# plt.show()


"""################OPTIONAL LOAD FROM FILE################"""
IQ = np.load('C:\\Users\\mallison\\Documents\\GitHub\\API_Sandbox\\IQ_data.npy')
fig2 = plt.figure(2, figsize=(20,10))
ax1 = fig2.add_subplot(211)
ax1.set_title('IQ Data')
ax1.plot(IQ)
ax2 = fig2.add_subplot(212)
ax2.set_title('Autocorrelation of IQ')
ax2.plot(signal.fftconvolve(IQ,IQ))
plt.show()

