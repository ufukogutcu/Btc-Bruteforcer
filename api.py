import random

api_providers = [
    'Blockchain.info',
    'Bitgo.com',
    'Blockchair.com',
    'Bitaps.com',
    'Bitcoinblockexplorers.com/v1',
    'Bitcoinblockexplorers.com/v2',
    'Blockstream.info',
    'Mempool.space',
    'Harari.blocksmurfer.io'
    ]

def balance(addr, provider):
    print(provider)
    if provider == 'Blockchain.info':
        #https://blockchain.info/
        return 1
    elif provider == 'Bitgo.com':
        #https://www.bitgo.com/api/v1/
        return 1
    elif provider == 'Blockchair.com':
        #https://api.blockchair.com/bitcoin/
        return 1
    elif provider == 'Bitaps.com':
        #https://api.bitaps.com/btc/v1/
        return 1
    elif provider == 'Bitcoinblockexplorers.com/v1':
        #https://bitcoinblockexplorers.com/api/v1/
        return 1
    elif provider == 'Bitcoinblockexplorers.com/v2':
        #https://bitcoinblockexplorers.com/api/v2/
        return 1
    elif provider == 'Blockstream.info':
        #https://blockstream.info/api/
        return 1
    elif provider == 'Mempool.space':
        #https://mempool.space/api/
        return 1
    elif provider == 'Harari.blocksmurfer.io':
        #https://harari.blocksmurfer.io/api/v1/btc/
        return 1
        
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
    