import collections
person = ('Sasha', 'Samus', 20, 'Barska', '01146')


Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'street', 'index'])
person1 = Person('Sasha', 'Samus', 20, 'Barska', '01146')
print(person1[0])
print(person1.name)
print(person1.last_name)
print(person1.age)
print(person1.street)
print(person1.index)

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)

mark_counts = collections.Counter(student_marks)
print(dict(mark_counts))


# черга deque
d = collections.deque()
d.append('last')
d.appendleft('first')
print(d)
d = collections.deque(maxlen=5)
d.append('1')
d.append('2')
d.append('last')
d.append('last')
d.append('last')
# тут має впасти
d.append('last')
d.append('something')
print(d)
