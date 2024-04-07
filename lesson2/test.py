# 1 умовне виконання - виконання якоїсь умови
# 2 цикли - повторення виконання блоку інструкцій поки виконується якась умова
# 3 винятки - виконання блоку інструкцій в випадку помилки


age = int(input('How old are you?: '))

if age > 18:
    print('You are > 18')
elif age == 18:
    print('Your age == 18')
else:
    print('You are infant yet!')

# if...elif...else


money = 0
if money:
    print('We have money')
else:
    print('No money')

# 0 -> False
# None -> False
result = None
if result:
    print(result)
else:
    print('Result is None')

# пустий контейнер, приводиться до False(наприклад '')

user_name = input('Input your name: ')

if user_name:
    print(f'Hello {user_name}')
else:
    print('Hello anonim!')


is_nice = True
state = 'nice' if is_nice else 'not nice'
if is_nice:
    state = 'nice'
else:
    state = 'not nice'
print(state)

a = int(input('Введіть число від 1 до 1000000'))

if a == 1:
    print('Число a == 1')
elif a == 2:
    print('Число a == 2')
elif a == 3:
    print('Число a == 3')
elif a == 4:
    print('Число a == 4')
elif a == 5:
    print('Число a == 5')


x = int(input('input x: '))
y = int(input('input y: '))

# if x == 0:
#     print("x can't be equal to zero")
#     x = int(input('x: '))
#     if x == 0:
#         print("x can't be equal to zero")
#         x = int(input('x: '))
#         if x == 0:
#             print("x can't be equal to zero")
#             x = int(input('x: '))
#             if x == 0:
#                 print("x can't be equal to zero")
#                 x = int(input('x: '))
#                 if x == 0:
#                     print("x can't be equal to zero")
#                     x = int(input('x: '))
#                     if x == 0:
#                         print("x can't be equal to zero")
#                         x = int(input('x: '))
#                         if x == 0:
#                             print("x can't be equal to zero")
#                             x = int(input('x: '))
#                             if x == 0:
#                                 print("x can't be equal to zero")
#                                 x = int(input('x: '))
#
# result = y / x

while x == 0:
    print("x can't be equal to zero")
    x = int(input('x: '))

result = y / x