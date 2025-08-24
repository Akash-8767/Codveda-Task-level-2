import apikey
import requests

headers = {
    'x-CMC_PRO_API_KEY': apikey,
    'accepts': 'application/ json'
}

params = { 
    'start' : '1'
    'limit': '5'
    'covert': 'USD'
}
url ='https://pro-api,coinmarket.com/v1/cryptocurrency/listings/latest'

json = requests.get(url,params,headers).json()

coins = json['data']

coin[0]

for x in coins:
    if x['symbol'] == 'BTC'
    x['quote']['USD']['price']

    print( x['symbol']), x['quote']['USD']['price'] 
