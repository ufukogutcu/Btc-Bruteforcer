from api import has_balance
from btc import generate_wallet

import threading
import time

def save(key, addr):
    with open("found.txt", "a") as file:
        file.write(f'Private key(int): {key}, Address: {addr}\n')

def run(start=1):
    key, addr = generate_wallet(start)
    if has_balance(addr):
        save(key, addr)

threads_running = False
cooldown = 0.1

def loop(start=1):
    global threads_running
    try:
        while threads_running:
            run(start)
            time.sleep(cooldown)
    except Exception as e:
        print(e)
        print('Error occured! Stopping Bruteforcer threads...')
        threads_running = False

def terminal():
    global threads_running
    global cooldown
    space = 4
    threads = [threading.Thread(target=loop)]
    help = '''Available commands:
- "start": Start the Bruteforcer
- "stop": Stop the Bruteforcer
- "info"|"i": Get information about the current status of the Bruteforcer
- "threads"|"th": Set the number of threads for the Bruteforcer to use
- "cooldown"|"cd": Set the number of seconds for each thread of the Bruteforcer to wait in between runs

- "probability"|"p": Learn about the probability of hitting an active address
- "exit"|"e": Exit the Bruteforcer
    '''
    
    print('Welcome to Bitcoin Bruteforcer by ufukogutcu!\n')
    print('Type "help" or "h" for a list of commands')
    
    while True:
        command = input('>')
        print('\n'*space)

        if command == 's':
            if threads_running:
                command = 'stop'
            else:
                command = 'start'

        #HELP
        if command in ['help','h']:
            print(help)

        #PROBABILITY
        elif command in ['probability','p']:
            print('''The Bitcoin address space is vast, with 2^160 possible addresses.
This number is so large that it's almost impossible to generate the same address as someone else.
ALMOST!
                  ''')

        #INFO
        elif command in ['info','i']:
            print(f'''Running: {str(threads_running)}
Number of threads: {str(len(threads))}
Cooldown: {str(cooldown)}s
        ''')

        #START
        elif command in ['start']:
            if threads_running:
                print('The Bruteforcer is already running!')
                continue
            print('Starting Bruteforcer...')
            threads_running = True
            for thread in threads:
                thread.start()
            print('Bruteforcer running!')

        #STOP
        elif command in ['stop']:
            if not threads_running:
                print('The Bruteforcer is not running!')
                continue
            print('Stopping Bruteforcer...')
            threads_running = False
            for thread in threads:
                thread.join()
            threads_number = len(threads)
            threads = [threading.Thread(target=loop) for i in range(threads_number)]
            print('Bruteforcer stopped!')

        #THREADS
        elif command in ['threads','th']:
            if threads_running:
                print('Number of threads can not be changed while the Bruteforcer is running!')
                continue
            threads_number = input('Please enter the number of threads for the Bruteforcer to use:')
            try:
                threads_number = int(threads_number)
            except:
                print('Number of threads has to be an integer or a float!')
                continue
            if threads_number < 1:
                print('Number of threads can not be less than 1!')
                continue
            threads = [threading.Thread(target=loop) for i in range(threads_number)]

        #COOLDOWN
        elif command in ['cooldown','cd']:
            if threads_running:
                print('Cooldown can not be changed while the Bruteforcer is running!')
                continue
            a = input('Please enter how many seconds each thread to wait for new address generation:')
            try:
                a = float(a)
            except:
                print('Cooldown has to be an integer or a float!')
                continue
            if a < 0:
                print('Cooldown can not be a negative number!')
                continue
            cooldown = a

        #EXIT
        elif command in ['exit','quit','q','e']:
            if threads_running:
                print('Stopping Bruteforcer threads before exiting...')
                threads_running = False
                for thread in threads:
                    thread.join()
                print('Bruteforcer stopped!')
            print('Thank you for using the Bitcoin Bruteforcer!')
            break

        else:
            print('Unrecognised command!')
            print('Type help or h for a list of commands')

if __name__ == '__main__':
    terminal()