'''
Пользователь вводит через дефис две буквы, Ваша задача написать программу, которая будет возвращать все символы между ними включительно.
Никаких проверок на ошибку делать не надо, минимальное значение всегда
меньше или равно максимальному.
Подсказка: Используйте модуль string , в котором есть string.ascii_letters, со всем набором необходимых букв
Пример:
"a-c" -> abc
"a-a" -> a
"s-H" -> stuvwxyzABCDEFGH
"a-A" -> abcdefghijklmnopqrstuvwxyzA
'''

import string
data = input("Ввод: ")
clean_data = data.replace("-", "")
start = min(clean_data)
end = max(clean_data)
letters = string.ascii_letters
s = letters.find(start)
e = letters.find(end)
res = letters[s:e+1]
if not res:
    res = letters[e:s + 1]
print(res)

