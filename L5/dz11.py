while True:
    number_1 = float(input("Введите число 1: "))
    number_2 = float(input("Введите число 2: "))
    type_operation = input("Выберите операцию (+ , - , / , *): ")

    number_1 = int(number_1)
    number_2 = int(number_2)

    if type_operation == "+":
        result = number_1 + number_2
        print(int(result))
    elif type_operation == "-":
        result = number_1 - number_2
        print(int(result))
    elif type_operation == "/":
        if number_2:
            result = number_1 / number_2
            print(int(result))
        else:
            print("Деление на ноль не определено")
    elif type_operation == "*":
        result = number_1 * number_2
        print(int(result))
    else:
        print("Ничего не выбрано")

    next_operation = input("Хотите продолжить?: ").lower()

    if next_operation != 'y':
        break




