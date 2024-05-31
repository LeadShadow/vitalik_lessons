# словники

numbers = {
    1: 'one',
    2: 'two',
    3: 'three'
}

for key in numbers:
    print(key)


for key in numbers.keys():
    print(key)

for value in numbers.values():
    print(value)

for key, value in numbers.items():
    print(key, value)


# множини

a = set()
print(a)

b = {1, 2, 3, 4}

print(b)

b.add(5)
print(b)

b.remove(5)
print(b)

b.discard(8)
print(b)


a = set('hello')
print(a)


b = set('hi there!')
print(b)

print(a & b)

print(a ^ b)

print(a | b)

# рядки
a = 'hello world'
b = "hello world"

print(a[0])
print(b[0])

# upper()
s = 'Hello'
s = s.upper()
print(s)

# lower()
s = 'Hello'
s = s.lower()
print(s)

# startswith()
s = '+380937316049'
if s.startswith('+380'):
    print('Цей номер український')

# endswith()
s = 'filinguk@gmail.com'
if s.endswith('@gmail.com'):
    print('Ця пошта від gmail')

a = [1, 2, 3, 4]
print(len(a))