'''
Напишите функцию-генератор generate_cube_numbers, которая формирует набор кубов чисел, начиная с числа 2 и
 до указанной Вами величины. Т.е. генератор должен работать до тех пор, пока генерируемое значение меньше указанной величины.

Напоминаю, что выйти из генератора можно с помощью return без параметров.

Например:

list(generate_cube_numbers(10)) - список с одним числом  [8], поскольку оно меньше 10.
list(generate_cube_numbers(100)) - [8, 27, 64] (5 в кубе это 125, а оно уже больше 100)

'''
def p(number, degree):
    return pow(number, degree)
def generate_cube_numbers(int_param):
    for i in range(2, int_param):
        start = i
        yield start
        start = p(start, 3)
    return

print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))