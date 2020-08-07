import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from datetime import timedelta
import pickle


sixMonth = timedelta(182)

# get data on this ticker
start = datetime(2020, 1, 1)

# Stores data in pickle file
faangmData = []
for i in ['FB', 'amzn', 'aapl', 'nflx', 'googl', 'msft']:
    microsoftTicker = yf.Ticker(i)
    msftHistory = microsoftTicker.history(period='1d', start=start, end=start + sixMonth, interval="60m")

    stockData = msftHistory["Open"].tolist()
    faangmData.append(stockData)

with open('FAANGM.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(faangmData, f, pickle.HIGHEST_PROTOCOL)

# the code below reads in the array.
# its shape is (6, 874). Facebook, amazon, apple, netflix, google, microsoft
"""

with open('FAANGM.pickle', 'rb') as f:
    data = pickle.load(f)

for i in data:
    print(i)

for i in data:
    print(i[-1], len(i))
"""
