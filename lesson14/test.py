from datetime import datetime
import random

day = datetime(year=2020, month=1, day=7, hour=14)
ts = day.timestamp()
print(ts)


day2 = datetime(year=2020, month=1, day=7, hour=14)
print(day2.strftime('%A %d %B %Y'))


s = '10 January 2020'
print(datetime.strptime(s, '%d %B %Y'))


# random
print(random.randint(1, 1000))
# rand -> random
# int -> ціле число

print(random.random())

fruits = ['apple', 'banana', 'orange']
random.shuffle(fruits)
print(fruits)

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))


fruits = ['apple', 'banana', 'orange']
print(random.choices(fruits, k=4))  # значення можуть повторюватись


fruits = ['apple', 'banana', 'orange']
print(random.sample(fruits, k=4))  # значення повторюватись не можуть!!!
