import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
from scipy.fft import fft
from scipy import interpolate
from datetime import datetime
from datetime import timedelta

a = datetime(2003, 8, 5)  # Sets up convenient time intervals for use
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
start = datetime(2019, 6, 7)

# bitcoin symbol is "btc-usd"
microsoftTicker = yf.Ticker("msft")
msftHistory = microsoftTicker.history(period='1d', start=start, end=today, interval="1h")

# for i in msftHistory:
#     print(msftHistory[i], i)
stockData = msftHistory["Open"].tolist()

teslaDownload = yf.download('TSLA', start='2019-01-01', end='2019-12-31', progress=False)
teslaDownload.head()

sns.set_style("dark")
sns.set_context("paper", font_scale=1.3, rc={"lines.linewidth": 1})
fig = plt.figure(num=None, figsize=(8, 3), dpi=80)
axes = fig.add_subplot()
axes.plot(stockData)
axes.grid()
fig.tight_layout()

plt.show()
