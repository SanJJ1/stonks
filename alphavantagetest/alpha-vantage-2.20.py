from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib.pyplot as plt
from alpha_vantage.techindicators import TechIndicators
import requests

api_key = 'CE5874ROQF7V2C3N'
'''
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
'''

# Company Overview

companyTickerName = input('Which ticker do you want information for?: ')
companyOverviewUrl = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={companyTickerName}&apikey={api_key}"

payload = {}
headers = {}

response = requests.request("GET", companyOverviewUrl, headers=headers, data=payload)

print(response.text.encode('utf8'))

# Income_Statement
incomeStatementUrl = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={companyTickerName}&apikey={api_key}"

payload = {}
headers = {}

response = requests.request("GET", incomeStatementUrl, headers=headers, data=payload)

print(response.text.encode('utf8'))

# Balance Sheet
balanceSheetUrl = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={companyTickerName}&apikey={api_key}"

payload = {}
headers = {}

response = requests.request("GET", balanceSheetUrl, headers=headers, data=payload)

print(response.text.encode('utf8'))

# Cash Flow
cashFlowUrl = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={companyTickerName}&apikey={api_key}"

payload = {}
headers = {}

response = requests.request("GET", cashFlowUrl, headers=headers, data=payload)

print(response.text.encode('utf8'))

# plt.show()
