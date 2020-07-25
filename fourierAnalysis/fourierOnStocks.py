import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
from scipy.fft import fft
from datetime import datetime
from datetime import timedelta

# sets up convenient time intervals for future use.
a = datetime(2003, 8, 5)
hour = timedelta(1 / 24)
sixHour = timedelta(1 / 4)
day = timedelta(1)
week = timedelta(7)
month = timedelta(30)
year = timedelta(365)
fiveYear = year * 5 + timedelta(2)
decade = fiveYear * 2 - timedelta(1)
timeIntervals = [hour, sixHour, day, week, month, year, fiveYear, decade]

today = datetime.today()

# get data on this ticker
start = datetime(2019, 12, 5)
stockTicker = yf.Ticker("tsla")
stockHistory = stockTicker.history(period='1d', start=start, end=today, interval="1h")

stockData = stockHistory["Open"].tolist()
print(stockData)

msft = yf.Ticker("msft").history(period='1d', start=start, end=today, interval="1h")["Open"].tolist()
print(msft)
# teslaDownload = yf.download('TSLA', start='2019-01-01', end='2019-12-31', progress=False)
# teslaDownload.head()

xAxis = np.linspace(0, 10000, len(stockData))
fftX = np.linspace(0, 100, 100)


# graph styling
sns.set_style("dark")
sns.set_context("paper", font_scale=1.3, rc={"lines.linewidth": 1})

# Adds plot
fig = plt.figure(num=None, figsize=(8, 3), dpi=80)
fig2 = plt.figure(num=None, figsize=(8, 3), dpi=80)

axes = fig.add_subplot()
axes2 = fig2.add_subplot()

# Graphs data
axes.plot(xAxis, stockData)
axes2.plot(xAxis, msft)


# Adds grid lines and compact layout
axes.grid()
axes2.grid()
fig.tight_layout()
fig2.tight_layout()

# axes2 = plt.figure(num=None, figsize=(8, 3), dpi=80).add_subplot()
# axes2.plot(fftX, [np.abs(fft(stockData))[i] for i in range(len(fftX))])
plt.show()
