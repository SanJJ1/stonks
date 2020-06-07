from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt
import math
# Number of sample points
# sample spacing
T = 1.0 / 5000
Interval = 1
N = int(Interval/T)

x = np.linspace(0.0, Interval, N)
y = np.sin(2.0 * math.pi * x)

yf = fft(y)
xf = np.linspace(0.0, 625, N//8)
plt.plot(x, 4.0/N * np.abs(yf))

axes2 = plt.figure().add_subplot().plot(x, y)
plt.grid()
plt.show()