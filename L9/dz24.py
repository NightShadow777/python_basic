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