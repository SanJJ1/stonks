import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
from scipy.fft import fft
from scipy import interpolate
from datetime import datetime
from datetime import timedelta

a = datetime(2003, 8, 5)
hour = timedelta(1/24)
sixHour = timedelta(1/6)
day = timedelta(1)
week = timedelta(7)
month = timedelta(30)
year = timedelta(365)
fiveYear = year*5 + timedelta(2)
decade = fiveYear*2 - timedelta(1)
timeIntervals = [hour,sixHour, day, week, month, year, fiveYear, decade]
for i in timeIntervals:
    print(a, a+i)


# get data on this ticker
start = datetime(2020, 5, 29)
microsoftTicker = yf.Ticker("MSFT")
msftHistory = microsoftTicker.history(period='1d', start=start, end=start + week, interval="1m")

# print(msftHistory)
# for i in msftHistory:
#     print(msftHistory[i], i)
stockData = msftHistory["Open"].tolist()

teslaDownload = yf.download('TSLA', start='2019-01-01', end='2019-12-31', progress=False)
teslaDownload.head()

xAxis = np.linspace(0, 10000, len(stockData))
fftX = np.linspace(0,100, 100)


sns.set_style("dark")
sns.set_context("paper", font_scale=1.3, rc={"lines.linewidth": 1})
# fig = plt.figure(num=None, figsize=(8, 3), dpi=80)
# axes = fig.add_subplot()
# axes.plot(xAxis, stockData)
# axes.grid()
# fig.tight_layout()

axes2 = plt.figure(num=None, figsize=(8, 3), dpi=80).add_subplot()
axes2.plot(fftX, [np.abs(fft(stockData))[i] for i in range(len(fftX))])
plt.show()