# Нагадаємо, що при отриманні рядків
#
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# Ми отримували наступний вивід:
#
# 380501233234
# 0503451234
# 0508889900
# 380501112222
# 380501112211
# Уявіть, що в іншому місці програми у нас виникла вимога зробити висновок у форматі
#
# +380501233234
# +380503451234
# +380508889900
# +380501112222
# +380501112211
# І тут ідеально підійде створення декоратора для функції sanitize_phone_number.
# Декоратор повинен додавати для коротких номерів префікс +38, а для повного міжнародного
# номера (з 12 символом) - тільки знак +. Реалізуйте декоратор format_phone_number для
# функції sanitize_phone_number з необхідним функціоналом.

def format_phone_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(result) == 12:
            return '+' + result
        elif len(result) == 10:
            return '+38' + result

    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number('(050)8889900'))
