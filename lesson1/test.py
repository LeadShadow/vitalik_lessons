# -> коментар
# user_age = 7
user_age = 18

# None, Числа, Boolean, String
# Числа(цілі, дробові, комплексні)
int_number = 3
float_number = 2.5
complex_number = 3.3 + 2j

# None - пустий тип

# Boolean -> булеве число
# a = 0, 1(False, True)

# and(*)
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

# or(+)
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False


# not(ні)
a = not True
print(a)

age = 18
adult1 = age >= 18
print(adult1)  # True

# print, id, input, bool, int, float, str, type
print('авфвфцвфцф')
input_number = int(input('Введіть число: '))  # int or not int?)
print(input_number)
print(type(input_number))
# input('Введіть число: ') -> int('20') -> 20 -> int
# приведення типів
print(input_number + 20)
# hello + 20
# try, except
# raises 28-11-2004

try:
    a = int('a')
except ValueError:
    print('НЕ МОЖНА ВВОДИТИ БУКВИ ЧИ ЯКІСЬ ТАМ СЛОВА')


# bool
# 1(функція bool буде приводити до False, такі типи як '', None, False, 0)
a = bool('a')  # True
print(a)
a = bool('')   # False
print(a)
a = bool(None)  # False
print(a)


# str
hello = 'Hello'
world = ' world'
print(hello + world)

# "" ''
print('can\'t')  # \' -> апостроф
print("can't")

# 0 1 2 3 4 5 6 7 8 9
print(hello[0])  # звернення по індексу
