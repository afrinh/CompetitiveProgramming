def Morse(x):
	d={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..'}
	list2=[]
	list3=[]
	count=0
	for i in x:
		if(len(i)!=1):
			list1=[]
			for j in i:
				list1.append(d[j])
			list2.append(''.join(list1))
		else:
			list2.append(d[i])

	# print list2

	for k in list2:
		# print k
		if k in list3:
			pass
		else:
			list3.append(k)
			count=count+1
	# print list3

	print count

x=input()

Morse(x)

