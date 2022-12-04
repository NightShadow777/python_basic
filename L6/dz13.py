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
print(string.ascii_letters)
data = input("Ввод: ")
start_letter = data[0]
end_letter = data[2]
letters = string.ascii_letters
s = letters.find(start_letter)
e = letters.find(end_letter)
res = letters[s+1:e]
print("{0}{1}{2}".format(start_letter, res, end_letter))