# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

import math
k = input('Введите первый символ:')
l = input('Введите второй символ:')
a = ord(k) - 96
b = ord(l) - 96
c = abs(a - b) - 1
print(f'{k} - {a} символ английского алфавита\n'
      f'{l} - {b} символ английского алфавита\n'
      f'Между {k} и {l} {c} букв')
