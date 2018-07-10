import unittest


def reverse(list_of_chars):

    # Reverse the input list of chars in place
    length=len(list_of_chars)
    if(length<2):
        return list_of_chars
    else:
        for i in range(length/2):
            temp=list_of_chars[i]
            list_of_chars[i]=list_of_chars[length-i-1]
            list_of_chars[length-i-1]=temp
            
    # print(list_of_chars)
        

    pass


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)