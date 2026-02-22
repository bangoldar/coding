def analyze_numbers(*args):  
    avarage = sum(args) / len(args)
    minimum = min(args)
    maximum = max(args)
    even = ()
    for arg in args:
        if arg % 2 == 0:
            even += (arg,)
    print(f'Sum: {sum(args)}\nAvarage: {avarage}\nMin: {minimum}\nMax: {maximum}\nEven numbers: {even}')

analyze_numbers(1,2,3,4,5,6)
