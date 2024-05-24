# зрізи

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]

print(odd_numbers, even_numbers, three_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:10:3]

numbers_copy = numbers[:]
print(numbers_copy)
print(numbers)

numbers_copy.append(11)
print(numbers_copy)
print(numbers)

# використання методів об'єктів
numbers1 = [1, 2, 3]
numbers1.append(4)  # добавляє елемент в кінець нашого списку
print(numbers1)

num = [1, 2]
num.clear()
print(num)


num = [1, 2]
num.remove(1)
print(num)

chars = ['a', 'b']
last = chars.pop(1)
print(chars)
print(last)


chars = ['a', 'b']
numbers = [1, 2, 3]
chars.extend(numbers)  # розширити список chars елементами зі списку numbers
print(chars)

chars = ['a', 'b']
chars.insert(1, 'c')
print(chars)


chars = ['a', 'b', 'c', 'd']
index = chars.index('c')
print(index)

chars = ['a', 'b', 'c', 'd', 'a', 'a']
a_count = chars.count('a')
print(a_count)


numbers = [1, 2, 3, 4, 6, 9, 3, 1, 10, 12, 46, 21]
numbers.sort()
print(numbers)

numbers = [1, 2, 3, 4, 6, 9, 3, 1, 10, 12, 46, 21]
numbers.sort(reverse=True)
print(numbers)

numbers = [1, 2, 3, 4, 6, 9, 3, 1, 10, 12, 46, 21]
numbers.sort()
numbers.reverse()
print(numbers)

nums = sorted(numbers)
print(nums)


# словники
chars = {'a': 1, 'b': 2}
b_num = chars.pop('b')
print(chars)
print(b_num)

chars = {'a': 1, 'b': 2}
chars.update({'c': 3})
print(chars)

chars = {'a': 1, 'b': 2}
chars.clear()
print(chars)

chars = {'a': 1, 'b': 2}
chars_copy = chars.copy()
print(chars_copy == chars)

chars = {'a': 1, 'b': 2}
c_index = chars.get('c', -1)
print(c_index)

chars = {'a': 1, 'b': 2}
c_index = chars['c']
print(c_index)
