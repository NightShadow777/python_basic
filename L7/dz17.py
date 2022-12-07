def correct_sentence(param):
    get_first_letter = param[:1]
    if get_first_letter.islower():
        word_list = []
        for w in param:
            if get_first_letter == w:
                w = w.replace(get_first_letter, w.upper())
                word_list.extend(w)
            else:
                word_list.extend(w)

        param = "".join(word_list)

    if "." in param:
        print(param)
    else:
        print(param + ".")

data  = input("Введите строку: ")
correct_sentence(data)