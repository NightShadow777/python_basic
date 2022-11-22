number_1 = float(input("Введите число 1: "))
number_2 = float(input("Введите число 2: "))
type_operation = input("Выберите операцию (+ , - , / , *): ")
next_math = ''

number_1 = int(number_1)
number_2 = int(number_2)

while True:
    if type_operation == "+":
        result = number_1 + number_2
        print(int(result))
        next_math = str(input("Хотите продолжить?: "))
    elif type_operation == "-":
        result = number_1 - number_2
        print(int(result))
        next_math = str(input("Хотите продолжить?: "))
    elif type_operation == "/":
        if number_2:
            result = number_1 / number_2
            print(int(result))
            next_math = str(input("Хотите продолжить?: "))
        else:
            print("Деление на ноль не определено")
            next_math = str(input("Хотите продолжить?: "))
    elif type_operation == "*":
        result = number_1 * number_2
        print(int(result))
    else:
        print("Ничего не выбрано")
        next_math = str(input("Хотите продолжить?: "))

    if next_math == 'y':
        continue
    else:
        break
