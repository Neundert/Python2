# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.int
import string

num = int(input('Введите номер буквы:'))
num = num - 1
print (string.ascii_lowercase[num])