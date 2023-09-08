from api import has_balance
from btc import generate_wallet

def save(key, addr):
    print(f'Saved: {key} {addr}')

def run(start=1):
    key, addr = generate_wallet(start)
    if has_balance(addr):
        save(key, addr)

if __name__ == '__main__':
    run(10000)