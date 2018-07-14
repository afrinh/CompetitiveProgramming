n=input()

i=0
count=0
while(i<len(n)-1):
	if(n[i]<n[i+1]):
		i=i+1
	else:
		for j in range(i+2,len(n)):
			if(n[j]>=n[i+1]):
				count=count+(n[j]-n[i+1])
				# +(n[i]-n[i+1])
				break
		i=i+1

print count



