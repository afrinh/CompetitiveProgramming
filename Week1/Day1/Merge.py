def merge_ranges(list1):
	x = sorted(list1, key=lambda tup: tup[0])
	new_list = []

	for tup in x:
		if not new_list:
			new_list.append(tup)
			# print(new_list)
		else:
			b = new_list.pop()
			# print(b)
			if b[1] >= tup[0]:
				if b[1]>tup[1]:
					new_tup = tuple([b[0], b[1]])
				else:	
					new_tup = tuple([b[0], tup[1]])
				new_list.append(new_tup)
				print(new_list)
			else:
				new_list.append(b)
				new_list.append(tup)
				print(new_list)
	# print(new_list)
	return new_list

l = [(1, 6), (3, 8), (4, 6), (10, 12),(9, 13)]
print("Original list: {}".format(l))
merged_list = merge_ranges(l)
print("After merge_ranges: {}".format(merged_list))
