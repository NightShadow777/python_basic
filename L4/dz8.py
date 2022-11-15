orign_list = [1, 3, 5]
#orign_list = [6]
#orign_list = []
sum_list = []
i = 0
while i <= len(orign_list):
    if not i % 2:
        if len(orign_list) == 0:
            orign_list.insert(0, i)
        sum_list.append(orign_list[i])
    i += 1
print(sum(sum_list) * orign_list[-1])
