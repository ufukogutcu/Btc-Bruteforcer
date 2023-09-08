from api import has_balance
from btc import generate_wallet

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

def save(key, addr):
    print(f'Saved: {key} {addr}')

def run():
    key, addr = generate_wallet()
    if has_balance(addr):
        save(key, addr)