# регулярні вирази
import re
s = 'I am 19 65464 years old'

age = re.search(r'\d+', s)
print(age.group())
# \d - всі цифри -> [0-9]
# \D - все окрім цифр
age = re.findall(r'\d+', s)
print(age)

s = 'blue socks and red shoes'
p = re.sub('(blue|white|red)', 'colour', s)
print(p)
# or -> |
