from datetime import datetime
import time
import json
import pandas as pd

def construct_download_url(
	ticker,
	period1,
	period2,
	interval='monthly'
):
	"""
	:period1 & period2: 'yyyy-mm-dd'
	:interval: {daily; weekly, monthly}
	"""
	def convert_to_seconds(period):
		datetime_value = datetime.strptime(period, '%Y-%m-%d')
		total_seconds = int(time.mktime(datetime_value.timetuple())) + 86400
		return total_seconds
	try:
		interval_reference = {'daily': '1d', 'weekly': '1wk', 'monthly': '1mo'}
		_interval = interval_reference.get(interval)
		if _interval is None:
			print('interval code is incorrect')
			return
		p1 = convert_to_seconds(period1)
		p2 = convert_to_seconds(period2)
		url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={p1}&period2={p2}&interval={_interval}&filter=history'
		return url
	except Exception as e:
		print(e)
		return

# retrive dataset
query_url = construct_download_url('BTC-USD', '2023-01-01', '2023-01-15', 'daily')
df = pd.read_csv(query_url)
df.set_index('Date', inplace=True)

# save dataset as a CSV
df.to_csv('Bitcoin Historical Data.csv')

# save dataset as a JSON file
with open('BTC-USD.json', 'w') as f:
	f.write(json.dumps(df.T.to_dict(), indent=4))