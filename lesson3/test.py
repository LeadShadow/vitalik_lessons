fruit = 'apple'

for char in fruit:
    print(char)


a = 1
while a <= 5:
    print(a)
    a = a + 1  # 1 + 1 -> 2 -> 2 + 1 -> 3


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a += 1


while True:
    user_input = input('Input something: ')
    print(user_input)
    if user_input == 'exit':
        break
# a % 2 -> if a % 2 -> ця умова виконається коли число непарне(a % 2 -> a % 2 -> 1
a = 0
while a < 6:
    a += 1
    if a % 2:
        print(a)
    else:
        continue


while True:
    number = int(input('number: '))
    while True:
        print(number)
        number -= 1
        if number < 0:
            break
    a = int(input('Input 0 if you want leave: '))
    if a == 0:
        print('Goodbye!')
        break


# Винятки
# механізм обробки винятків
try:
    int('a')
except Exception as e:
    print(e)


val = 'a'
try:
    val = int(val)
except ValueError:
    print(f'value {val} is not a number')
else:
    print(val > 0)
finally:
    print('This will be printed anyway')


