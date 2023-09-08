import requests
from api import has_balance

test_addr_active = '3K5wTxuoQWcUZmjpSB2FVg33ETTFrb6DQX'
test_addr_null = '1N7iX8v8Wh4Poi9owrNQTre8sPEU2KNHzh'

api_providers = [
    'https://blockchain.info/',
    'https://www.bitgo.com/api/v1/',
    'https://api.blockchair.com/bitcoin/',
    'https://api.bitaps.com/btc/v1/',
    'https://bitcoinblockexplorers.com/api/v1/',
    'https://bitcoinblockexplorers.com/api/v2/',
    'https://blockstream.info/api/',
    'https://mempool.space/api/',
    'https://harari.blocksmurfer.io/api/v1/btc/'
    ]

print('Addr 1:')
print(has_balance(test_addr_active))

print('Addr 2:')
print(has_balance(test_addr_active))