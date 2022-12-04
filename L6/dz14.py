data = input("Ввод: ")
if int(data) > 0:
    s = 1
    while True:
        s = 1
        for n in data:
            s *= int(n)
        data = str(s)
        print(data)
        if int(data) <= 9:
            break
else:
    print("Stop!")