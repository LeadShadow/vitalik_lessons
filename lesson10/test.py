import shutil
from pathlib import Path
# робота з файлами
# файловий дескриптор

fh = open('test_file.txt')
fh.close()

# w -> відкриття на запис, якшо файлу не існує, створює його
# r -> читання з файлу(значення за замовчуванням)
# x -> відкриття на запис, якшо файлу не існує, то буде виняток
# a(append) -> відкриття на дозапис
# b -> відкриття в двійковому форматі
# t -> те саме шо r
# + -> і запис і читання

fh = open('test_file.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test_file.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test_file.txt', 'r')
first_two_symbols = fh.read(2)
print(first_two_symbols)

fh.close()

fh = open('test_file.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()

fh = open('test.txt', 'w')
fh.write('first line\n'
         'second line\n'
         'third line')
fh.close()

fh = open('test.txt')
while True:
    line = fh.readline()
    if not line:
        break
    print(line, end='')

fh.close()

fh = open('test.txt')
lines = fh.readlines()
print()
print(lines)

fh = open('test.txt')
try:
    # some_manipulation(fh)
    print('daw')
finally:
    fh.close()

with open(Path('C:/Users/pc/Desktop/заняття/vitalik_lessons/test1.txt')) as fh:
    print(fh)


# робота з архівами
acrhive_name = shutil.make_archive('backup', 'zip')
shutil.unpack_archive(acrhive_name, 'new_folder_for_data')