from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib.pyplot as plt
from alpha_vantage.techindicators import TechIndicators


api_key = 'CE5874ROQF7V2C3N'

#getting stock info
ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(4))
#Graphing stock data
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')


#Technical indicators- Bollinger Bands
ti = TechIndicators(key=api_key, output_format='pandas')
data1, meta_data1 = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data1.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')

plt.show()

#Company Overview
import requests

function = input('Which ticker: ')
url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={function}&apikey=CE5874ROQF7V2C3N"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

