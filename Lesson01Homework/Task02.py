time_seconds = int(input('Введите время в секундах: '))

hours = time_seconds // 3600
print(hours)
minutes = (time_seconds % 3600)//60
print(minutes)
seconds = time_seconds - hours * 3600 - minutes * 60
print(seconds)

print("{:>2}ч:{:>2}м:{:>2}с".format(hours, minutes, seconds))