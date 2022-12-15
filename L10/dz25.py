def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    i = 0
    while True:
        if i < end:
            yield begin
            begin = func(begin)
        else:
            break
        i += 1

print(list(some_gen(2, 4, pow)))
print(list(some_gen(2, 6, pow)))
print(list(some_gen(2, 10, pow)))
print(list(some_gen(3, 12, pow)))