from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

today = datetime.today()

# get data on this ticker
start = datetime(2019, 12, 5)
msft = yf.Ticker("msft").history(period='1d', start=start, end=today, interval="1h")["Open"].tolist()

# creates a signal with components listed in the variable freqComps
x = msft



# takes the left side of the discrete Fourier Transform
y = fft(x)[:len(x) // 2]

# takes the inverse Fourier Transform of y, expected to result in x.
# yinv = ifft(y)

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
plt.plot(np.linspace(0, 1000, len(x)), x, color=c["red"])



# plt.plot(basis[:numSamples//2], np.real(yinv) / 2 - 2, ".")  # Inverse Inverse FTT
# fourierGraphs = [(np.abs(y), "green"), (np.real(y), "blue"), (np.imag(y), "yellow"), (np.zeros(numSamples), "black")]

# Creates a linear space ?????????????????
xAxis = np.linspace(0, 100, len(y))

# Graphs the Fourier Transform. Has to multiply by two since the other half of the transform
# is cut off. Divides by numSamples because the number of samples increases the magnitude.
yAxis = np.abs(y) * 2 / len(x)

# Creates a second window for the results of the dft on the signal displayed
# in the first window.
axes2 = plt.figure().add_subplot()
axes2.plot(xAxis, yAxis)

plt.show()
