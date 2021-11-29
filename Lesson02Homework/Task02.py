a = list(input('Введите значения списка без пробелов и символов-разделителей: '))
n = len(a) - 1

for i in range(0, n, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)
