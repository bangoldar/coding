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
import random
import string

length = 10
numbers = True
letters = True
specSymbols = False
quant = 1

def settings():
    global length, numbers, letters, specSymbols, quant
    while True:
        choice = input(
            f'1. length ({length})\n'
            f'2. numbers ({numbers})\n'
            f'3. letters ({letters})\n'
            f'4. specSymbols ({specSymbols})\n'
            f'5. quant ({quant})\n'
            f'press enter to exit\n'
            f'>> '
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
            quant = int(input('quant: '))
        elif choice == '':
            break
        else:
            print('enter valid choice')

def generate():
    actualSymbols = ''
    if numbers:
        actualSymbols += string.digits
    if letters:
        actualSymbols += string.ascii_letters
    if specSymbols:
        actualSymbols += string.punctuation

    if actualSymbols == '':
        return print('No symbols selected')
        
    passwords = []

    for _ in range(quant):
        password = ''
        for _ in range(length):
            password += random.choice(actualSymbols)
        passwords.append(password)

    for p in passwords:
        print(p)

def start():
    while True:
        choice = input('press 1 for settings, press 2 to generate, press enter to exit\n>> ')
        if choice == '1':
            settings()
        elif choice == '2':
            generate()
        elif choice == '':
            break
        else:
            print('enter valid choice')

start()