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

    w = []
    for word in data:
        w.extend(word)

    #не может начинаться с цифры
    #не может состоять только из цифр
    #не может содержать заглавные буквы
    #не может содержать знаки пунктуации
    #не может содержать зарегистрированные слова keyword.kwlist
    for char in w:
        if data[:1].isdigit():
            print(False)
        elif data.isdigit():
            print(False)
        elif char.isalpha() and char.isupper():
            print(False)
        elif char in symbol:
            print(False)
        elif w in keyword.kwlist:
            print(False)
        else:
            print(True)

else:
    print("Введите переменную для проверки")