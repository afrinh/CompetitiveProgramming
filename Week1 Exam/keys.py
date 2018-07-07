list1=input()
list2=[]
length=len(list1)

for i in range(0,length-1):
	if(list1[i]==(type)(list)):
		for i in list1[i]:
			list2.append(list1[i][i])
		# print(list[i])
	else:
		x=list1[i]
		# val=list1[x]
		print(x)
		# list2.append(val)

for i in list2:
	if i in list1:
		print('true')
	else:
		print('false')

