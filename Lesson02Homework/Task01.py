
user = {'name': 'Kate', 'age': 25}
numbers = [1, 2, 3]
tuple = ('name', 'surname', 'age')
set = {2.3, 7.4, 6.5}
list = [5, 'World', 7.3, True, user, numbers, tuple, set]

for i in list:
    print(f'{i} is {type(i)}')
