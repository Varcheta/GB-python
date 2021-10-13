ernings = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
profit = round(ernings - costs, 3)                    #вычисляем прибыль
profitability = round(profit / ernings, 3)           #вычисляем рентабельность выручки


if ernings > costs:
    employee_qty = int(input('Введите кол-во сотрудников компании: '))
    employee_profit = round(profit / employee_qty, 3)     #прибыль на 1 сотрудника
    print('Прибыль компании составила {}. Рентабельность выручки = {}. Прибыль на 1 сотрудника = {}'.format(profit, profitability, employee_profit))
elif ernings == costs:
    print('Компания работает в 0')
else:
    print('Компания работает в убыток. Потери составили {}'.format(profit))