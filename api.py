import random
import requests

api_providers = [
    'Blockchain.info',
    'Blockchair.com',
    'Bitaps.com',
    'Bitcoinblockexplorers.com/v1',
    'Bitcoinblockexplorers.com/v2',
    'Blockstream.info',
    'Mempool.space',
    'Harari.blocksmurfer.io'
    ]

def balance(addr, provider):
    if provider == 'Blockchain.info':
        #https://blockchain.info/ #multiple
        response = requests.get(f'https://blockchain.info/balance?active={addr}')
        try:
            return int(response.json()[addr]['final_balance'])
        except:
            return False
    elif provider == 'Blockchair.com':
        #https://api.blockchair.com/bitcoin/ #multiple
        response = requests.get(f'https://api.blockchair.com/bitcoin/addresses/balances?addresses={addr}')
        try:
            data = response.json()['data']
            if not data:
                return 0
            return int(data[addr])
        except:
            return False
    elif provider == 'Bitaps.com':
        #https://api.bitaps.com/btc/v1/
        return False
    elif provider == 'Bitcoinblockexplorers.com/v1':
        #https://bitcoinblockexplorers.com/api/v1/
        return False
    elif provider == 'Bitcoinblockexplorers.com/v2':
        #https://bitcoinblockexplorers.com/api/v2/
        return False
    elif provider == 'Blockstream.info':
        #https://blockstream.info/api/
        return False
    elif provider == 'Mempool.space':
        #https://mempool.space/api/
        return False
    elif provider == 'Harari.blocksmurfer.io':
        #https://harari.blocksmurfer.io/api/v1/btc/
        response = requests.get(f'https://harari.blocksmurfer.io/api/v1/btc/address_balance/{addr}')
        try:
            # Harari currently not working
            return False
        except:
            return False
        
    return False

def has_balance(addr):
    random.shuffle(api_providers)
    for provider in api_providers:
        bal = balance(addr, provider)
        if bal is False:continue
        if bal > 0:
            return True
        return False
    raise Exception('All providers failed!')
    
if __name__ == '__main__':
    test_addr_active = '3K5wTxuoQWcUZmjpSB2FVg33ETTFrb6DQX'
    test_addr_null = '1N7iX8v8Wh4Poi9owrNQTre8sPEU2KNHzh'

    print(balance(test_addr_active, 'Blockchair.com'))
    print(balance(test_addr_null, 'Blockchair.com'))