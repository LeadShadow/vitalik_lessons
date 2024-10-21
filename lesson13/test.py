# datetime, random, collections
from datetime import datetime, timedelta
# основні можливості datetime
# 1) визначення поточної дати і часу
# 2) обчислення інтервалу між двома подіями
# 3) визначення дня тижня
# 4) порівняння дати і часу декількох подій
# 5) робота з часовими зонами
# 6) перетворення дати/часу в рядок і навпаки

# list, dict, string, int, float
a = datetime.now()
print(type(a))  # 2024-10-18 20:26:11.520346
b = input('Input something: ')
print(type(b))  # '2024-10-18 20:26:11.520346'
print(a == b)

current_datetime = datetime.now()
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

print(current_datetime.date())
print(current_datetime.time())


date1 = datetime(year=2022, month=2, day=24, hour=5)
print(date1)

print(date1.weekday())  # 0 - понеділок, 6 - неділя

future_month = (current_datetime.month % 12) + 1
future_year = current_datetime.year + 1
future_datetime = datetime(future_year, future_month, 1)
print(current_datetime < future_datetime)
print(current_datetime)
print(future_datetime)


date1 = datetime(year=2022, month=2, day=24)
date2 = datetime(year=2023, month=2, day=24)


print(date2 - date1)
print(date2 + timedelta(30))


current_datetime = datetime.now()
print(current_datetime + timedelta(weeks=23))
