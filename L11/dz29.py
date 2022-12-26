def generate_cube_numbers(int_param):
    for i in range(2, int_param):
        res = pow(i, 3)
        if res < int_param:
            yield res
        else:
            return

print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))