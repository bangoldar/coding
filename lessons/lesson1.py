'''
"if" - T
"and etc" - T
"+-" - T
"while, for" - T
'''

### while ###
'''
n = 5

while n != 0:
    # n = 5, 4, 3, 2, 1, 0
    print(n)
    n -= 1
'''

# 0 2 4 6 .. 20

'''
n = 0

while n <= 20:
    print(n)
    n += 2
'''


# ui = input('Hello!\n>>')

# while ui != 'hello':
#     ui = input('Hello!\n>>')


'''

Menu:  
 - 1. Parity Check 
 - 0. Exit
>> 0
Goodbye!

Menu:  
 - 1. Parity Check 
 - 0. Exit
>> 1

Your number: 5
It was odd!

Menu:  
 - 1. Parity Check 
 - 0. Exit
>> 

'''

'''
choice = 1

while choice != 0:
    print(
        'Menu:',
        ' - 1. Parity Check',
        ' - 0. Exit',
        sep='\n'
        )    
    
    choice = int(input('Enter choice: '))     

    if choice == 1:
        number = int(input('Your number: '))
        
        if number % 2 == 0:
            print('Your number is even!')
        elif number % 2 != 0:
            print('Your number is odd!')

    elif choice not in (1, 0):
        print("Select valid choice.")    

print('Goodbye!')  
'''



### for loop ###

# nums = range(10) # 0-9

# for num in nums:
#     print(num)


# nums = range(5,11) # 5-10

# for num in nums:
#     print(num)

nums = range(5,11,2) # 5-10 po 2

for num in nums:
    print(num)