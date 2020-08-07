from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
'4YFNRPL4DM78QYDY'
# Simply sets the colors to be used when graphing
c = {"red": (255, 0, 0),
     "green": (0, 255, 0),
     "blue": (0, 0, 255),
     "yellow": (255, 238, 0),
     "black": (0, 0, 0)}
for i in c:
    c[i] = [rgbVal / 255 for rgbVal in c[i]]

testdata = ['3', '5', '9', '3', '8', '13', '3', '6', '7', '1', '1', '2', '1', '3', '9', '8', '6', '11', '9', '5', '4', '5', '4', '8', '2', '3', '11', '10', '6', '6', '5', '8', '14', '5', '8', '9', '12', '7', '7', '10', '10', '11', '11']
testdata = [int(i) for i in testdata]
# Sets the number of samples to be used in the dft (Discrete Fourier Transform)
# numSamples = len(testdata)
numSamples = 500

# Sets the frequency (the spacing) of the samples in the dft
sampleFrequency = 750 ** -1

# Creates what essentially becomes the rgbVal-axis for the dft
basis = np.linspace(0, sampleFrequency * numSamples, num=numSamples + 1)

# frequency components for square wave below. Each element in the array is an array
# of length two where the first element is the amplitude  of the wave and the second is the
# frequency of the wave.
# freqComps = [[1, 73], [1, 33], [2, 90], [2, 140], [1, 7]]
freqComps = [[1, 21], [1, 55], [1, 9]]

# creates a signal with components listed in the variable freqComps
signal = sum([i[0] * np.sin(basis * 2 * np.pi * i[1]) for i in freqComps]) + 1
print(signal[:9])


# takes the left side of the discrete Fourier Transform
y = fft(signal)[:numSamples // 2]

# y = testdata[:numSamples // 2]
# takes the inverse Fourier Transform of y, expected to result in rgbVal.
yinv = ifft(y)



# Plots the axes and the graph of the signal to be analyzed
plt.axhline(y=0, color=c["black"])
plt.axvline(x=0, color=c["black"])
plt.plot(signal, color=c["red"])
plt.plot(yinv, color=c["green"])


# plt.plot(basis[:numSamples//2], np.real(yinv) / 2 - 2, ".")  # Inverse Inverse FTT
# fourierGraphs = [(np.abs(y), "green"), (np.real(y), "blue"), (np.imag(y), "yellow"), (np.zeros(numSamples), "black")]


# Graphs the Fourier Transform. Has to multiply by two since the other half of the transform
# is cut off. Divides by numSamples because the number of samples increases the magnitude, so this offsets that.
# np.abs is used because the complex must be cut off.
transform = np.abs(y) * 2 / numSamples
print(transform[:9])
transform_imag = np.imag(y) * 2 / numSamples

# Creates a linear space ?????????????????
xAxis = np.linspace(0, sampleFrequency ** -1, num=numSamples + 1)[:numSamples // 2]


# Creates a second window for the results of the dft on the signal displayed
# in the first window.
axes2 = plt.figure().add_subplot()
axes2.plot(xAxis, transform, color=c["red"])
axes2.plot(xAxis, transform_imag, color=c["yellow"])



plt.show()
