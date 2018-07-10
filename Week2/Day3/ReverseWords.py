import unittest

def reverse_words(message):
    first=0
    count=0
    last=len(message)
    if(len(message)==0):
        return
    revstring = rev(message,first,last)
    for i in range(len(message)):
        if message[i]!=' ':
            count=count+1
        else:
            last=i
            count=0
            rev(message,first,last)
            first=last+1
    if(i==len(message)-1):
        rev(message,first,len(message))
            
    print(''.join(message))
    
def rev(message,first,last):
    if(last<2):
        return message
    else:
        k=(int)(first+(last-first)/2)
        step=0
        for j in range(first,k):
            message[j],message[last-step-1]=message[last-step-1],message[j]
            step=step+1
    return message











# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)