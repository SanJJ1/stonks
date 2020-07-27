from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
import math
# Number of sample points
# sample spacing
T = 1.0 / 50000
Interval = 1
N = int(Interval/T) + 1

x = np.linspace(0.0, Interval, N)
y = np.sin(20 * math.pi * x)

yf = fft(y)[0:N//15]
xf = np.linspace(0.0, 6, N//15)
plt.plot(xf,  np.abs(yf)/N)
plt.plot(xf, np.real(ifft(yf)))
axes2 = plt.figure().add_subplot().plot(x, y)
plt.grid()
plt.show()