# вивчити!!!
# strip(), replace(), removepreffix(), removesuffix(), format()

# Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних
# керівних символів: [\n, \f, \r, \t, \v]
#
# Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:
#
# 'Alex\nKdfe23\t\f\v.\r'
# 'Al\nKdfe23\t\v.\r'
# ps: можна зробити використовуючи метод replace
import re


def real_len(string1: str):
    cleaned_string = string1.replace('\n', '')\
        .replace('\f', '')\
        .replace('\r', '')\
        .replace('\t', '')\
        .replace('\v', '')
    return len(cleaned_string)


print(real_len('Alex\nKdfe23\t\f\v.\r'))


def real_len(string1: str):
    return len(re.sub(r'\n|\f|\r|\t|\v', '', string1))


print(real_len('Alex\nKdfe23\t\f\v.\r'))
