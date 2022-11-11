number_1 = float(input("Введите число 1: "))
number_2 = float(input("Введите число 2: "))
type_operation = input("Выберите операцию (+ , - , / , *): ")

if type_operation == "+":
    result = int(number_1) + int(number_2)
    print(result)
elif type_operation == "-":
    result = int(number_1) - int(number_2)
    print(result)
elif type_operation == "/":
    if number_2:
        result = int(number_1) / int(number_2)
        print("Делитель не равен 0")
        print(result)
    else:
        print("Делитель равен 0")
elif type_operation == "*":
    result = int(number_1) * int(number_2)
    print(result)
else:
    print("Ничего не выбрано")