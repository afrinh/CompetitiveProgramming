def QueueReconstruction(list1):
	list2=[[0,0]]*len(list1)
	for i in list1:
		for j in list2:
			if(i[0]>=j[0] and i[1]>=j[1]):
				index=i[1]
				for i in range(list2,0):
					temp=i
					


				list2[index]=i
				print list2








list1=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
QueueReconstruction(list1)
