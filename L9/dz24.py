'''
Дан массив чисел (float или/и int). Вам нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом.
Ваша функция difference должна уметь работать с неопределенным количеством аргументов. Если аргументов нет, то функция возвращает 0 (ноль).

Вх. данные: Переменное число аргументов как числа (int, float).

Вых. данные: Разница между максимумом и минимумом как число (int, float).

Примеры:

difference (1, 2, 3) == 2
difference (5, -5) == 10
difference (10.2, -2.2, 0, 1.1, 0.5) == 12.4
difference () == 0
'''

def difference(*args):
    if args:
        min_element = args[0]
        max_element = args[-1]
        for element in args:
            if element < min_element:
                min_element = element

            if element > max_element:
                max_element = element
        result = max_element - min_element
        return result
    else:
        result = 0
        return result

print(difference (1, 2, 3))
print(difference (5, -5))
print(difference (10.2, -2.2, 0, 1.1, 0.5))
print(difference ())