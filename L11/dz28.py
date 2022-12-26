def prime_generator(int_param):
    for i in range(2, int_param + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i
print(list(prime_generator(10)))