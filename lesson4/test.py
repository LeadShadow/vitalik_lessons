# ООП програмування
# функціональне програмування

# функції

print('dawdaw')
# функція це як прораб

def say_hello():
    print('Привіт! Світ')


say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()

def print_max(a, b):
    if a > b:
        print(f'a={a} максимальне')
    elif a == b:
        print('a == b')
    else:
        print(f'b={b} максимальне')


print_max(3, 5)
print_max(6, 1)
a = print_max(1, 1)
print(a)

# return
def plus(a, b):
    return a + b

print(plus(3, 5))

x = 50

def func():
    x = 2
    print(f'Заміна глобального х на {x}')


func()
print(f'x все ще {x}')


def func():
    global x
    x = 2
    print(f'Заміна глобального х на {x}')

func()
print(f'Значення x == {x}')

x = 50
def func():
    x = 2
    print(f'Заміна глобального х на {x}')
    return x

x = func()
print(f'Значення x == {x}')


# ключеві аргументи

def func(a, b=5, c=10):
    print(f'a == {a}, b == {b}, c == {c}')  #


func(10)
func(10, 10)
func(10, c=12)
func(10, b=10, c=12)
func(a=15, b=10, c=12)

def say(message, times=1):
    print(message * times)


say('Привіт')
say('Світ', 5)


# змінне число параметрів
def total(a=5, *numbers, **phone_book):
    print(a)
    for item in numbers:  # (1, 2, 3, 4, 5)
        print(f'item == {item}')

    for name, number in phone_book.items():  # phone_book - словник
        print(f'{name}: {number}')


total(10, 1, 2, 3, 4, 5, Sasha='+380937316049', Misha='+380937316043')  # позиційні через кому, без передачі по імені, ключеві по назві аргументу


# кортежі
my_tuple = tuple()
another_tuple = ()

not_empty = (1, 2, 3, 4)
count = 0
for i in not_empty:
    print(i)
    count += i

print(count)
print(not_empty[0])
print(not_empty[1])
print(not_empty[2])
print(not_empty[3])
