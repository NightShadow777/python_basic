'''
Функция second_index принимает в качестве параметров 2 строки. Вам необходимо найти индекс второго вхождения искомой строки в строке для поиска.
Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims". Если бы нам надо было найти ее первое вхождение,
то тут все просто: с помощью функции index или find мы можем узнать, что "s" – это самый первый символ в слове "sims", а значит индекс
первого вхождения равен 0. Но нам необходимо найти вторую "s", а она 4-ая по счету. Значит индекс второго вхождения (и ответ на вопрос) равен 3.
Строка, которую нужно найти, может состоять из нескольких символов.

Input: Две строки (String).
Output: Int or None

Примеры:
second_index("sims", "s") => 3
second_index("find the river", "e") => 12
second_index("hi", "h") => None
'''

def second_index(istring, wanted_symbol):
    if istring and wanted_symbol:
        result = None
        for i, s in enumerate(istring):
            if i > 0 and wanted_symbol in s:
                result = i
    else:
        result = "Error!"
    return result

istring = input("Введите строку: ")
wanted_symbol = input("Символ для поиска: ")
s_index = second_index(istring, wanted_symbol)
print(s_index)