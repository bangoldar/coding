'''
Задача:
    Написать программу для генерации паролей.
    В рамках программы должна присутсвовать настройка генерации,
    так же должный быть базовые значения для них.
    Список настроек:
        - длинна пароля (базовая 10)
        - перечень символов (
            базовая:
                numbers-true,
                letters-true,
                specSymbols-false
                )
        - количество паролей за одну генерацию (базовая 1)'''
import random, string

length = 10
numbers = True
letters = True
specSymbols = False
quant = 1

def settings():
    global length, numbers, letters, specSymbols, quant
    while True:
        choice = input(
            f'1. length ({length})',
            f'2. numbers ({numbers})',
            f'3. letters ({letters})',
            f'4. specSymbols ({specSymbols})',
            f'5. quant ({quant})',
            'press enter to exit'
            '>>',
            sep='\n'
        )
        if choice == '1':
            length = int(input('length: '))
        elif choice == '2':
            numbers = not numbers
        elif choice == '3':
            letters = not letters
        elif choice == '4':
            specSymbols = not specSymbols
        elif choice == '5':
            quant = not quant
        elif choice == '':
            break
        else:
            print('enter valid choice')
        

        
        letters = bool(input('letters (true/false): '))
        specSymbols = input('specSymbols (true/false): ')
        quant = input('quant: ')

def generate():
    passwords = ()

    actualSymbols = ''
    if numbers:
        actualSymbols += string.digits
    if letters:
        actualSymbols += string.ascii_letters
    if specSymbols:
        actualSymbols += string.punctuation
    for _ in range(quant): # pass 1
        password = ''
        for _ in range(length):
            password += random.choice(actualSymbols)
        passwords += password
    print


            
        

   

def start():
    while True:
        choice = input('press 1 for settings, press 2 to generate')
        
        if choice == 1:
            settings() 
        elif choice == 2:
            generate()
        else:
            print('enter valid choice')

start()