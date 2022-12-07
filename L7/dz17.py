def correct_sentence(param):
    if param:
        result = ""
        word_list = []
        i = 0
        for w in param:
            if i == 0 and w.islower():
                w = w.title()
                word_list.extend(w)
            else:
                word_list.extend(w)
            i += 1
        join_list = "".join(word_list)

        if "." in join_list:
            result = join_list
        else:
            result = join_list + "."
        return result
    else:
        return "Введите строку!!!"

data  = input("Ввод: ")
run = correct_sentence(data)
print(run)