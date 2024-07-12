# Завдання: Напишіть програму, яка перевіряє, чи є введений рядок дійсним
# українським мобільним номером телефону. Український мобільний номер має
# наступний формат: +380xxxxxxxxx, де x - це цифра від 0 до 9, інші символи
# не допускаються.
#
# Приклад вхідних даних:
#
# "+380971234567"
# "380661234567"
# "+380 (50) 123-45-67" -> "380501234567"
# "123456789"
import re
from task1 import sanitize_phone_number
phone_numbers = [
    "+380971234567",
    "380661234567",
    "+380 (50) 123-45-67",
    "123456789",
    "0937316049",
    '0501243567'
]


def validate_ukrainian_number(phone_number: str):
    pattern = r'^(380|0)\d{9}$'
    sanitized_phone_number = sanitize_phone_number(phone_number)
    p1 = re.search(pattern, sanitized_phone_number)
    print(p1.group())
    return bool(re.search(pattern, sanitized_phone_number))


print(validate_ukrainian_number('+380971234567'))
