import re
def anagram(s,t):
	s=s.lower()
	t=t.lower()
	s=re.sub('[^a-zA-Z]','',s)
	t=re.sub('[^a-zA-Z]','',t)
	s=set(s)
	t=set(t)
	# print(s)
	# print(t)
	count=0
	for each in s:
		if each in t and each!=' ':
			count=count+1
		else:
			count=0
	# print(count)
	if(count==max(len(s),len(t))):
		print('true')
	else:
		print('false')
s=raw_input()
t=raw_input()
anagram(s,t)

