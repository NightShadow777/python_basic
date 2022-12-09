def find_unique_value(param):
    if param:
        for p in param:
            c = param.count(p)
            if c == 1:
                result = p
        return result

print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3]))
print(find_unique_value([5, 5, 5, 0.5]))