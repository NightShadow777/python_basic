def correct_sentence(param):
    if param:
        join_list = param[0].title() + param[1:]
        if not "." in join_list[-1]:
            join_list = join_list + "."
        return join_list
    else:
        return "Введите строку!!!"

data  = input("Ввод: ")
run = correct_sentence(data)
print(run)