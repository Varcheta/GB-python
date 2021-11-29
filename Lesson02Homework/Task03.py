# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


# 1 Решение через list:
season = ['Зима', 'Весна', 'Лето', 'Осень']
months = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

month_1 = int(input('Введите любой номер месяца от 1 до 12: '))

for i in zip(season, months):
    if month_1 in i[1]:
        print(i[0])

if month_1 not in range(1, 12 + 1):
    print('Указанный номер месяца не существует')

# 2 Решение через dict:
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month_number2 = int(input('Введите любой номер месяца от 1 до 12: '))

for key, value in seasons.items():
    if month_number2 in value:
        print(key)

if month_number2 not in range(1, 12 + 1):
    print('Указанный номер месяца не существует')