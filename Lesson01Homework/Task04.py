value1 = int(input('Введите целое положительное число: '))
max_value = 0

while value1 > 0:
    value2 = value1 % 10
    if max_value < value2:
        max_value = value2
    value1 //= 10
print(max_value)
