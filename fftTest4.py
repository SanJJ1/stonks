from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

c = {"red": (255, 0, 0),
     "green": (0, 255, 0),
     "blue": (0, 0, 255),
     "yellow": (255, 238, 0),
     "black": (0, 0, 0)}
for i in c:
    c[i] = [x / 255 for x in c[i]]

numValues = 1000
sampleSpacing = 1/10000
basis = np.linspace(0, sampleSpacing * numValues, num=numValues)
x = np.sin(basis * 2 * np.pi * 1) + np.sin(basis * 2 * np.pi * 10)
y = fft(x)
yinv = ifft(y)

plt.plot(x, color=c["red"])

fourierGraphs = [(np.abs(y), "green"), (np.real(y), "blue"), (np.imag(y), "yellow"), (np.zeros(numValues), "black")]

axes2 = plt.figure().add_subplot()

for i in fourierGraphs:
    axes2.plot(i[0][:int(numValues*.01)]/numValues, color=c[i[1]])


plt.show()
