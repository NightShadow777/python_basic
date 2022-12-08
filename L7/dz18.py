def second_index(istring, wanted_symbol):
    string_index = istring.find(wanted_symbol, istring.find(wanted_symbol) + 1)
    if string_index == -1:
        string_index = None
    print(string_index)

istring = input("Введите строку: ")
wanted_symbol = input("Символ для поиска: ")
second_index(istring, wanted_symbol)