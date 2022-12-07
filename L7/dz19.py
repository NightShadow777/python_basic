def common_elements(param_one, param_two):
    t_multiples = [n for n in range(0, param_one, 3)]
    f_multiples = [n for n in range(0, param_two, 5)]
    t_multiples = set(t_multiples)
    f_multiples = set(f_multiples)
    result = t_multiples.intersection(f_multiples)
    return result

param_one = int(input("Кол-во с числами кратными 3: "))
param_two = int(input("Кол-во с числами кратными 5: "))
c_elements = common_elements(param_one, param_two)
print(c_elements)