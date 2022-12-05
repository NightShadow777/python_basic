data = input("Ввод: ")
if int(data) > 0:
    s = 1
    while True:
        s = 1
        for n in data:
            s *= int(n)
        data = str(s)
        if int(data) <= 9:
            break
    print(data)
else:
    print("Stop!")