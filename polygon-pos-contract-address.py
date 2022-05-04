import json
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# curl -X 'GET'  'https://api.coingecko.com/api/v3/asset_platforms'  -H 'accept: application/json' | jq .
# data = cg.get_asset_platforms()
# print(data)
# # list = json.loads(data)
# # print(list)
# curl -X 'GET' \
  # 'https://api.coingecko.com/api/v3/coins/polygon-pos/contract/0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270' \
  # -H 'accept: application/json'

# curl -X 'GET' \
#   'https://api.coingecko.com/api/v3/coins/polygon-pos/contract/0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270' \
#   -H 'accept: application/json' | jq .market_data.current_price.usd
# data = cg.get_coin_info_from_contract_address_by_id('polygon-pos','0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270')
# data = cg.get_coin_info_from_contract_address_by_id("polygon-pos","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270")
# print(data)

# curl -X 'GET' \
#   'https://api.coingecko.com/api/v3/simple/token_price/polygon-pos?contract_addresses=0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270&vs_currencies=USD' \
#   -H 'accept: application/json'

print(cg.get_token_price('polygon-pos','0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270','USD'))