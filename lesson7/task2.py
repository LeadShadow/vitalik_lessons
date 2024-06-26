# Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні.
# Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику.
# Першим параметром у функцію ми передаємо словник, а другим — значення, що
# хочемо знайти. Таким чином, результат може бути як список ключів, так і порожній
# список, якщо ми нічого не знайдемо.
# {'1': 'one', '2': 'one', '3': 'one'}
def lookup_key(data: dict, value):
    result = []  # result - список ключів
    for key in data:
        if data[key] == value:  # data[key] -> value
            result.append(key)
    return result


print(lookup_key({'1': 'one', '2': 'two', '3': 'two'}, 'two'))
