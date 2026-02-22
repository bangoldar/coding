


### functions ###


# def show_data(age: int | None = 0, name: str | None = ''):
#     name = name.title()
#     print(f'name: {name}')
#     print(f'age: {age}')

# show_data(
#     name = 'alex',
#     age = 10)


'''
Задача:
    Написать функцию: "show_range", она будет принимать в себя два аргумента:
        - start_stop: tuple[int,int] (это кортеж, где лежат два numbers)
        - mode: str ("up","down" это направление, в котором должен двигаться наш диапазон)
    
    Твоя функция должна на основое режима работы,
    сформировать и вывести на экран диапазон чисел.
    Пример:
        show_range((10,1)) #up
            1 2 3 4 5 6 7 8 9 10
        show_range((10,1),mode="down")
            10 9 8 7 6 5 4 3 2 1
        show_range((1,1)) 
            два числа одинаковы
'''


def show_range(start_stop: tuple[int, int], mode: str | None = "up"):
    biggest = max(start_stop)
    smallest = min(start_stop)
    if biggest != smallest:
        if mode == 'up':
            print(*range(smallest, biggest+1))
        elif mode == 'down':
            print(*range(biggest, smallest-1, -1))
        else:
            print('Enter valid option')
    else:
        print('numbers are alike')

# show_range((10, 1), mode="down")
# show_range((10, 1))

### range ###

# import random as r

# num = r.randint(1,10)
# args = (3,2,1,"hello",True)
# r_arg = r.choice(args)

# print(r_arg)
 

 