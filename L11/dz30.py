def is_even(param):
    if int(param) == param:
        some_var = param >> 1
        if param == (some_var << 1):
            return True
        else:
            return False
    else:
        return "Число нецелое..."

print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))
print()

#test
print(is_even(2))
print(is_even(5))
print(is_even(0))
print()

print(is_even(2.1))
print(is_even(2.3))

