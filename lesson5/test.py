# словник
from test1 import say_hello
# Саша - +380937316048

# число, рядок, кортеж

empty_dict = {}
another_empty_dict = dict()
print(empty_dict, another_empty_dict)

some_dict = {
    'key': 'value',
    1: 'one'
}

not_empty = {'key': 'value'}
not_empty['new_key'] = 'new_value'


# рекурсивна функція
# 5! -> 5 * 4! -> 5 * 4 * 3! -> 5 * 4 * 3 * 2! -> 5 * 4 * 3 * 2 * 1
def factorial(n: int) -> int:
    """Ця функція обраховує факторіал числа"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# 5 * factorial(4) -> 5 * 4 * factorial(3)

print(factorial(5))

number = 5
result = 1
while number >= 1:
    result = result * number
    number -= 1

print(result)

if __name__ == "__main__":
    say_hello('Sasha')


# Структури даних - 4-й розділ
# список
my_list = list()

empty_list = []

not_empty = [1, 2, 'user']

print(not_empty[0])
print(not_empty[1])
print(not_empty[2])
# print(not_empty[3])

not_empty[1] = 'user1'
print(not_empty)

# зрізи(slice)
some_str = 'This is awesome string'
first_five = some_str[0:5]
print(first_five)
print(not_empty[0:2])
