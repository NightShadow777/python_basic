import string
import keyword
data = input("Type string: ")

if data:
    symbol =[]
    for s in string.punctuation:
        if s == '_':
            del_symbol = s.replace("_", "")
        else:
            del_symbol = s
        symbol.extend(del_symbol)

    word = []
    upper_word = []
    lower_word = []
    check_symbol = False

    for w in data:
        word.extend(w)
        if w.isupper():
            upper_word.extend(w)
        else:
            lower_word.extend(w)

        if w in symbol:
            check_symbol = True

    upper_word = "".join(upper_word)
    lower_word = "".join(lower_word)

    if data[:1].isdigit():
        print(False)
    elif data.isnumeric():
        print(False)
    elif upper_word.isupper():
        print(False)
    elif check_symbol:
        print(False)
    elif lower_word in keyword.kwlist:
        print(False)
    else:
        print(True)
else:
    print("Введите переменную для проверки")