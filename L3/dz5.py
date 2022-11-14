'''
[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
[1, 2, 3] => [[1, 2], [3]]
[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
[1] => [[1], []]
[] => [[], []]
'''
a = [1,2,3,4,5,6]
#a = [1,2,3,4,5]
#a = [1,2,3]
#a = [1]
#a = []
new_list = []
number = len(a)
if (number % 2) == 0:
	#print("четное")
	indx = number // 2
	new_list.append(a[:indx])
	new_list.append(a[indx:])
	print(new_list)
else:
	#print("нечетное")
	indx = (number // 2)+1
	new_list.append(a[:indx])
	new_list.append(a[indx:])
	print(new_list)