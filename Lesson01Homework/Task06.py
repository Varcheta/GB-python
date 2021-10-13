a = float(input('Кол-во км в 1-й день: '))
b = float(input('Цель в км: '))
day_number:int = 1

while a < b:
    a = a*1.1
    day_number = day_number + 1
print(day_number)