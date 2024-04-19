# Перевірка паролю
password = ''
count = 0
while password != 'password12345':
    password = input('Введіть пароль: ')
    count += 1
    if count == 3:
        print('Спробуйте ввести пароль пізніше')
        break
    if 'password12345' == password:
        print('Ви увійшли в систему')

