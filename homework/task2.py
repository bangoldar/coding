def check_access(*ages):
    adults = 0
    minors = 0
    for age in ages:
        if age >= 18:
            adults+=1
        elif age < 18:
            minors+=1
    print(f'minors: {minors}\nadults: {adults}')
    if len(ages) == adults:
        print('access granted')
    else:
        print('access denied')

check_access(20, 19, 56, 34)