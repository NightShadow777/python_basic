def second_index(istring, wanted_symbol):
    if istring and wanted_symbol:
        result = None
        for i, s in enumerate(istring):
            if i > 0 and wanted_symbol == s:
                result = i
    else:
        result = "Error!"
    return result

istring = input("Введите строку: ")
wanted_symbol = input("Символ для поиска: ")
s_index = second_index(istring, wanted_symbol)
print(s_index)