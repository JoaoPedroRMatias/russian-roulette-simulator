from random import randint
import os
import time

time.sleep(1)

with open('txt/ascii.txt', 'r', encoding='utf-8') as f:
    bottoken = f.read()

print(bottoken)
dec = str(input('Rolar a roleta? (s / n)\n'))

if dec == 'n':
    print('\n---------------------------------------------------------------------')
    print('                            TCHAU MEDROSO!')
    print('---------------------------------------------------------------------\n')
    time.sleep(3)

if dec == 's':
    x = randint(1,6)

    if x == 6:
        print('\n---------------------------------------------------------------------')
        print('                            MORTO! Tchau tchau rsrs')
        print('---------------------------------------------------------------------\n')
        time.sleep(3)
        os.system(f"shutdown /s /t 2")
    
    if x != 6:
        print('\n---------------------------------------------------------------------')
        print('                            VIVO!')
        print('---------------------------------------------------------------------\n')
        time.sleep(3)