import urllib.request
import time
import json
from datetime import datetime

price_eth_usd = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'
save_file = open(datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '.dat', 'w')
while True:
	try:
		res = urllib.request.urlopen(price_eth_usd).read()
		res_json = json.loads(res.decode("utf-8"))
		time_price = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(res_json['USD'])]
		res_text = str('\t'.join(time_price))
		save_file.write(res_text + '\n')
		print(res_text)
	except Exception as e:
		print(str(e))
	time.sleep(1)

save_file.close()