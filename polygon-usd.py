import requests
import math
import json
import sys

# List given coins & its price in SGD

base_url = "https://api.coingecko.com/api/v3"

# url = base_url + "/coins/list"
# r = requests.get(url)
# identifiers = r.json()
# symbol_id_map = {d["symbol"]:d["id"] for d in identifiers}
# symbols = ["MATIC"]
# ids = [symbol_id_map[symbol.lower()] for symbol in symbols]
# ids = ",".join(ids)
# print (ids)
# print(f"Arguments of the script : {sys.argv[1:]=}")
# ids = sys.argv[1]
# print (ids)
# url = base_url + f"/simple/price?ids={ids}&vs_currencies=sgd"
ids = 'matic-network'
url = base_url + f"/simple/price?ids={ids}&vs_currencies=USD"
r = requests.get(url)
# print('TYPE: ' , type(r))
print(r.json())
data = r.json()
prices = data['matic-network']['usd']
print(prices)
one = abs (math.remainder(1.035, prices))
print (one)