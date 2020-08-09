import shelve
import json
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

companyTickerName = input('Which ticker do you want information for?: ')

#Company Overview

companyOverviewUrl = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={companyTickerName}&apikey={api_key}"

payload = {}
headers= {}

companyOverviewEncoded = requests.request("GET", companyOverviewUrl, headers=headers, data = payload).text.encode('utf8')


#Income_Statement
incomeStatementUrl = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={companyTickerName}&apikey={api_key}"

payload = {}
headers= {}

incomeStatementEncoded = requests.request("GET", incomeStatementUrl, headers=headers, data = payload).text.encode('utf8')


#Balance Sheet
balanceSheetUrl = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={companyTickerName}&apikey={api_key}"

payload = {}
headers = {}

balanceSheetEncoded = requests.request("GET", balanceSheetUrl, headers=headers, data = payload).text.encode('utf8')


#Cash Flow
cashFlowUrl = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={companyTickerName}&apikey={api_key}"

payload = {}
headers = {}

cashFlowEncoded = requests.request("GET", cashFlowUrl, headers=headers, data = payload).text.encode('utf8')


#Shelving info
with shelve.open('allStats') as stats:
    stats['companyOverview'] = companyOverviewEncoded
    stats['incomeStatement'] = incomeStatementEncoded
    stats['balanceSheet'] = balanceSheetEncoded
    stats['cashFlow'] = cashFlowEncoded

'''
#Printing from the shelve
with shelve.open('allStats') as stats:
    for i in stats:
        print(i, stats[i])
'''

#Getting Specific Data
with shelve.open('allStats') as stats:
    loadOverview = json.loads(stats['companyOverview'].decode('utf8'))
    '''
    for i in loadOverview:
        allInfoList= list(loadOverview[i])
    print('Available Info: ' + allInfoList)
    '''
    whatInfo = input('What Info do you want?:').strip()
    print(f'{whatInfo}: ' + loadOverview[f'{whatInfo}'])

#plt.show()
