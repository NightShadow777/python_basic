def find_unique_value(param):
    if param:
        for p in param:
            c = param.count(p)
            if c == 1:
                result = p
        return result

i_data = input("Input num: ").split()
print(find_unique_value(i_data))