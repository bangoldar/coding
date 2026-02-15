'''
Y n: 5

5 * 1 = 5
5 * 2 = 10
...
5 * 10 = 50

'''

# start = int(input('enter number: '))

# nums = range(1, 11)

# for num in nums:
#     print(start, "*", num, '=', num*start)

# age = 16
# name = 'Alex'

# print('Name:',name)
# print('Age:',age)




# temp = '|{:^10}|{:^5}|'

# print('-'*18)
# print(temp.format('Name','Age'))
# print('-'*18)

# for _ in range(5):
#     print(temp.format(name,age))

# print('-'*18)



### functions ###

# def show_data():
#     print('ha-ha')

# show_data()
# show_data()
# show_data()
# show_data()


# def show_data(name:str,age:int):
#     name = name.lower()
#     print(f'Name: {name}\nAge: {age}')

# show_data(30,'Petr')
# show_data(age=30,name='Dima')


# start, end 5, 20 (5,6,7,...,20)

# def counter(start, end):
#     nums = range(start, end+1)
#     for num in nums:
#         print(num)

# counter(4, 20)

# def a():
#     return 123

# b = a()


# def get_summ(*args:int):
#     for n in args:
#         print(n)


# get_summ(3,2,1,4)

t = (1,4,7,2,1)
print(t.count(4))
print(t.index(1))
print(t.index(1,1))