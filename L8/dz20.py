def add_one(param=None):
    if not param is None:
        num = ""
        for n in param:
            num += str(n)
        result = int(num) + 1
        result = [l for l in str(result)]
        return result


print(add_one())
print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9, 9]))
print(add_one([0]))
print(add_one([9]))