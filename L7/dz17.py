def correct_sentence(param):
    if param:
        get_first_letter = param[:1]
        word_list = []
        i = 0
        for w in param:
            if i == 0:
                w = w.replace(get_first_letter, w.upper())
                word_list.extend(w)
            else:
                word_list.extend(w)
            i += 1
        param = "".join(word_list)

        if "." in param:
            print(param)
        else:
            print(param + ".")
    else:
        print("Введите строку!!!")

data  = input("Ввод: ")
correct_sentence(data)