def generate_cube_numbers(int_param: int) -> int:
    '''функция-генератор generate_cube_numbers, которая формирует набор кубов чисел,
    начиная с числа 2 и до указанной Вами величины. '''
    for i in range(2, int_param):
        res = pow(i, 3)
        if res < int_param:
            yield res
        else:
            return

print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))

print(list(generate_cube_numbers(1000)))
print(list(generate_cube_numbers(2000)))