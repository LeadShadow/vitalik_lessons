# функція як об'єкт першого класу

def func(x, y):
    return x + y


func_alias = func
result = func_alias(2, 3)
print(result)


def func1(func, x):
    return func(2, 3) + x


print(func1(func, 3))


# область видимості
SOME_VAR = 3


def func(x):
    SOME_VAR = x
    print(SOME_VAR)


func(4)
print(SOME_VAR)


# замикання
def adder(value):
    def inner(x):
        return x + value
    return inner


two_adder = adder(2)  # inner
print(two_adder(3))  # inner(3), value = 2

# каррування


# def handle_operation(x, y, operator):
#     if operator == '-':
#         return x - y
#     elif operator == '+':
#         return x + y
#
#
# print(handle_operation(10, 20, '+'))
# Позбавляємось такого варіанту

def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}


def get_handle(operator):
    return OPERATIONS[operator]  # повертається функція яку в подальшому викликаємо


handler = get_handle('-')
print(handler(2, 9))
