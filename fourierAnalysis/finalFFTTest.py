from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt


# Sets the number of samples to be used in the dft (Discrete Fourier Transform)
numSamples = 10000

# Sets the frequency (the spacing) of the samples in the dft
sampleFrequency = 3200 ** -1

# Creates what essentially becomes the x-axis for the dft
basis = np.linspace(0, sampleFrequency * numSamples, num=numSamples + 1)


# frequency components for square wave below. Each element in the array is an array
# of length two where the first element is the amplitude  of the wave and the second is the
# frequency of the wave.
freqComps = [[1, 800], [1, 40]]

# creates a signal with components listed in the variable freqComps
x = sum([i[0] * np.sin(basis * 2 * np.pi * i[1]) for i in freqComps])

# takes the left side of the discrete Fourier Transform
y = fft(x)[:numSamples // 2]

# takes the inverse Fourier Transform of y, expected to result in x.
yinv = ifft(y)

# Simply sets the colors to be used when graphing
c = {"red": (255, 0, 0),
     "green": (0, 255, 0),
     "blue": (0, 0, 255),
     "yellow": (255, 238, 0),
     "black": (0, 0, 0)}
for i in c:
    c[i] = [x / 255 for x in c[i]]

# Plots the axes and the graph of the signal to be analyzed
plt.axhline(y=0, color=c["black"])
plt.axvline(x=0, color=c["black"])
plt.plot(basis, x, color=c["red"])


# plt.plot(basis[:numSamples//2], np.real(yinv) / 2 - 2, ".")  # Inverse Inverse FTT
# fourierGraphs = [(np.abs(y), "green"), (np.real(y), "blue"), (np.imag(y), "yellow"), (np.zeros(numSamples), "black")]

# Creates a linear space ?????????????????
xAxis = np.linspace(0, sampleFrequency ** -1, num=numSamples + 1)[:numSamples // 2]

# Graphs the Fourier Transform. Has to multiply by two since the other half of the transform
# is cut off. Divides by numSamples because the number of samples increases the magnitude.
yAxis = np.abs(y) * 2 / numSamples

# Creates a second window for the results of the dft on the signal displayed
# in the first window.
axes2 = plt.figure().add_subplot()
axes2.plot(xAxis, yAxis)

plt.show()
