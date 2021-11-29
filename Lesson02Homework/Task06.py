# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# from pprint import pprint
goods = []
count = 1
parameters = ['название', 'цена', 'количество', 'eд']
while input('Добавить новый товар? Введите ответ (да/нет)>>> ') == 'да':
    product = {i: input(f"Введите {i}: ") for i in parameters}
    goods.append((count, product))
    count += 1
# pprint(goods)

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
num = {'название': set(), 'цена': set(), 'количество': set(), 'eд': set()}
for _, product in goods:
    num['название'].add(product['название'])
    num['цена'].add(product['цена'])
    num['количество'].add(product['количество'])
    num['eд'].add(product['eд'])

for k, v in num.items():
    num[k] = list(v)
print(num)