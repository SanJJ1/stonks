from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
import sympy.ntheory as nt

c = {"red": (255, 0, 0),  # Formats colors
     "green": (0, 255, 0),
     "blue": (0, 0, 255),
     "yellow": (255, 238, 0),
     "black": (0, 0, 0)}
for i in c:
    c[i] = [x / 255 for x in c[i]]

# Start of Fourier analysis
numSamples = 320
sampleFrequency = 320 ** -1
basis = np.linspace(0, sampleFrequency * numSamples, num=numSamples + 1)

freqComps = [[1, 80], [1, 40]]  # frequency components for square wave.
x = sum([i[0] * np.sin(basis * 2 * np.pi * i[1]) for i in freqComps])  # creates signal with components of freqComps

print(basis)
print(x)
y = fft(x)[:numSamples // 2]
yinv = ifft(y)

plt.axhline(y=0, color=c["black"])
plt.axvline(x=0, color=c["black"])
plt.plot(basis, x, color=c["red"])
# plt.plot(basis[:numSamples//2], np.real(yinv) / 2 - 2, ".")  # Inverse Inverse FTT


# fourierGraphs = [(np.abs(y), "green"), (np.real(y), "blue"), (np.imag(y), "yellow"), (np.zeros(numSamples), "black")]

axes2 = plt.figure().add_subplot()
axes2.plot(np.linspace(0, sampleFrequency ** -1, num=numSamples + 1)[:numSamples // 2], np.abs(y) * 2 / numSamples)

plt.show()
