a = int(input('Введите количество минут: '))
b = int(a / 60)

duration_hours = a - b * 60
if b < 2:
    hours = ("час")
elif b >= 2 and b <= 4:
    hours = ("часа")
else: hours = ("часов")


print(f"Событие будет идти {b} {hours} и {duration_hours} минут")
