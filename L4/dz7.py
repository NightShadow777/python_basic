orign_list = [0, 1, 0, 3, 12]
#orign_list = [0]
#orign_list = [1, 0, 3, 0, 0, 0, 5]
#orign_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
number_list = []
null_list = []
for element in orign_list:
    if element > 0:
        number_list.append(element)
    else:
        null_list.append(element)
number_list.extend(null_list)
print(number_list)