from random import randint
import os
import time

time.sleep(1)

with open('txt/asciiGun.txt', 'r', encoding='utf-8') as f:
    gun = f.read()

print(gun)
dec = str(input('Rolar a roleta? (s / n)\n'))

if dec == 'n':
    print('\n---------------------------------------------------------------------')
    print('                            TCHAU MEDROSO!')
    print('---------------------------------------------------------------------\n')
    time.sleep(3)

if dec == 's':
    x = randint(0,5)

    if x == 0:
        print('\n---------------------------------------------------------------------')
        print('                            MORTO! Tchau tchau rsrs')
        print('---------------------------------------------------------------------\n')
        time.sleep(3)
        os.system(f"shutdown /s /t 2") #FIM
        
    if x != 0:
        print('\n---------------------------------------------------------------------')
        print('                            VIVO!')
        print('---------------------------------------------------------------------\n')
        
        for i in range(5):
            nDec = str(input('{} voltas e você vence. Roletar novamente? (s / n)\n'.format(5-i)))

            if nDec == 'n':
                print('\n---------------------------------------------------------------------')
                print('                            TCHAU MEDROSO!')
                print('---------------------------------------------------------------------\n')
                time.sleep(3)
                break
 
            if nDec == 's':
                x = randint(0,5)

                if x == 0:
                    print('\n---------------------------------------------------------------------')
                    print('                            MORTO! Tchau tchau rsrs')
                    print('---------------------------------------------------------------------\n')
                    time.sleep(3)
                    os.system(f"shutdown /s /t 2") #FIM

                if x != 0:
                    print('\n---------------------------------------------------------------------')
                    print('                            VIVO!')
                    print('---------------------------------------------------------------------\n')

        print('Parabéns, você saiu vivo!')
        with open('txt/asciiWin.txt', 'r', encoding='utf-8') as f:
            win = f.read()
        print(win)
        print('\n---------------------------------------------------------------------')

        time.sleep(3)