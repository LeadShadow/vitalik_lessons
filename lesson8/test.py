# перевірка на входження

a = [1, 2, 3, 4, 5]
if 4 in a:
    print('4 лежить в списку а')

b = 'hello world'
if 'hello' in b:
    print('hello in b')

print('------------------------------------------------------------------')

# кількість елементів
hello_world = 'hello world'
print(len(hello_world))

print('------------------------------------------------------------------')

# перебір усіх елементів в циклі for
for i in a:
    print(i)


print('------------------------------------------------------------------')
# спеціальні символи
# \n - перенос рядка
# \f - перенесення сторінки
# \r - повернення каретки
# \t - горизонтальна табуляція
# \v - вертикальна табуляція
print('Hello world\nHello world')
print('Hello world\rHello world654')

# find

s = '+380937316049'
start = 0
end = 11
print(s.find('+', start, end))
print(s.find('+'))
# rfind
# index

s = 'I am learning strings in Python. Some new methods got now.'
sentences = s.split('. ')
print(sentences)

s1 = '. '.join(sentences)
print(s1 == s)

# strip(), replace(), removepreffix(), removesuffix(), format()
