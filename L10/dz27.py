def is_even(param):
    if int(param) == param:
        if (param % 2) == 0:
            return True
        else:
            return False
    else:
        return "Число нецелое..."

print(is_even(2))
print(is_even(5))
print(is_even(0))
print(is_even(2.1))
print(is_even(2.3))