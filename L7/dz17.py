def correct_sentence(param):
    if param:
        word_list = []
        i = 0
        for w in param:
            if i == 0 and w.islower():
                w = w.title()
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