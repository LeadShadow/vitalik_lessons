# def complicated(x, y):
#     return x / y
#
#
# def logged_func(func):
#     def inner(x, y):
#         print(f'called with {x}, {y}')
#         result = func(x, y)
#         print(f'result: {result}')
#         return result
#     return inner
#
#
# complicated_ = logged_func(complicated)
# complicated_(10, 20)


def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


@logged_func
def complicated(x, y):
    return x / y


complicated(10, 20)


def our_range(x, y):
    while x < y:
        yield x
        x += 1


#five_to_ten_generator = interval_generator(5, 10)
#print(list(five_to_ten_generator))
# print(next(five_to_ten_generator))
# print(next(five_to_ten_generator))
# print(next(five_to_ten_generator))
# print(next(five_to_ten_generator))
# print(next(five_to_ten_generator))
# print(next(five_to_ten_generator))
#print(next(five_to_ten_generator))

for i in our_range(5, 10):
    print(i)

print('------------------------')
for i in range(5, 10):
    print(i)

# лямбда функції
sum_lambda = lambda x, y: x + y
print(sum_lambda(10, 20))
print('--------------------------------')
# map
numbers = [1, 2, 3, 4, 5]
names = ['oleksandr', 'misha', 'vasya', 'vitalii']
for i in map(lambda x: x ** 2, numbers):
    print(i)

print(list(map(lambda x: x ** 2, numbers)))

print(list(map(lambda x: x.title(), names)))

names_title = []
for i in names:
    names_title.append(i.title())
print(names_title)

names_title = [i.title() for i in names]
print(names_title)


for i in filter(lambda x: x % 2, range(1, 11)):
    print(i)

print(list(filter(lambda x: x % 2, range(1, 11))))
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))

print(list(filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers))))

num1 = []
for i in numbers:
    a = i ** 2
    if a % 2 == 0:
        num1.append(a)

print(num1)