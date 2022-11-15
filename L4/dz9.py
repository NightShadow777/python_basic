#orign_list = [1, 2, 3, 4, 5, 6, 7, 9]
#orign_list = [1, 1, 1, 1]
#orign_list = [6, 3, 7]

import random
new_list = []
orign_list = [l for l in range(random.randint(3, 10))]
print("Origin list: ", end="")
print(orign_list)
new_list.append(orign_list[0])
new_list.append(orign_list[2])
new_list.append(orign_list[-2])
print("New list: ", end="")
print(new_list)