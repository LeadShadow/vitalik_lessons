# Завдання: Повторення рядку
#
# Напиши програму, яка приймає від користувача рядок тексту та ціле число N,
# і виводить цей рядок тексту N раз.

text = input('Input something: ')

n = int(input('Input N: '))

while n > 0:
    print(text)
    n -= 1

n = int(input('Input N: '))
for i in range(n):  # range(3) -> 0, 1, 2
    print(text)

