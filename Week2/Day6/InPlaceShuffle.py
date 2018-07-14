import random
def shuffle(the_list):
    length=len(the_list)
    for i in range(length-1,0,-1):
        j = random.randint(0,i)
        the_list[i],the_list[j] = the_list[j], the_list[i]
        
        

    # Shuffle the input in place



sample_list = [1, 2, 3, 4, 5]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list