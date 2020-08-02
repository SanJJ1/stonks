from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

#getting stock info
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))

