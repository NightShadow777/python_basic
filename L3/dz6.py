#my_list = [12, 3, 4, 10]
#my_list = [1]
#my_list = []
my_list = [6, 5, 3, 1]
my_list = [6, 5, 3, 1, 10, 40, 35]

if len(my_list) > 1:
    get_el = my_list.pop()
    my_list.insert(0, get_el)
    print(my_list)
else:
    print(my_list)
