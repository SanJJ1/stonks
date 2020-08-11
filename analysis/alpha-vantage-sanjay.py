import requests
import shelve
import datetime
import json
import pprint as pp
api_key = 'CE5874ROQF7V2C3N'
# Sanjay's API key: '4YFNRPL4DM78QYDY'

def get_time_series(ticker='TSLA', interval=3):
    intervals = ['INTRADAY', 'DAILY', 'DAILY_ADJUSTED', 'WEEKLY', 'WEEKLY_ADJUSTED', 'MONTHLY', 'MONTHLY_ADJUSTED']
    time_interval = "TIME_SERIES_" + intervals[interval]

    time_series_url = f"https://www.alphavantage.co/query?function={time_interval}&symbol={ticker}&apikey={api_key}"

    payload = {}
    headers = {}

    response = requests.request("GET", time_series_url, headers=headers, data=payload)

    time = datetime.datetime.now().strftime('%Hh-%d-%m-%Y')

    with shelve.open('stock_data') as db:
        db[f"{ticker} - {intervals[interval]}"] = json.loads(response.text.encode('utf8'))

    return response


# get_time_series()

with shelve.open('stock_data') as db:
    for i in db:
        print(i, db[i])
