import random
orign_list = [random.randint(3, 10) for l in range(random.randint(3, 10))]
#orign_list = [1, 2, 3, 4, 5, 6, 7, 9]
#orign_list = [1, 1, 1, 1]
#orign_list = [6, 3, 7]
print("First list: ", end="")
print(orign_list)
print("Second list: ", end="")
print(orign_list[0], orign_list[2], orign_list[-2])