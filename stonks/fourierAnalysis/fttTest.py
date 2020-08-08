from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt
import math
# Number of sample points
N = 6000
# sample spacing
T = 1.0 / 5000.0
x = np.linspace(0.0, N*T, N)
y = np.sin(261.626 * 2.0 * math.pi * x) + np.sin(329.628 * 2.0 * math.pi * x) + np.sin(39.995 * 2.0 * math.pi * x)
yf = fft(y)
xf = np.linspace(0.0, 625, N//8)

plt.plot( 4.0/N * np.abs(yf))

plt.grid()
plt.show()