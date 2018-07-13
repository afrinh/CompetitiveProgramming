import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    len1=len(my_list)
    len2=len(alices_list)
    new_list=[]
    # print(my_list)
    # print(alices_list)
    i=0
    j=0
    while(i<len1 and j<len2):
        if(my_list[i]<alices_list[j]):
            new_list.append(my_list[i])
            i=i+1
        else:
            new_list.append(alices_list[j])
            j=j+1
            
    if(i>=len1):
        while(j<len2):
            new_list.append(alices_list[j])
            j=j+1
    else:
        while(i<len1):
            new_list.append(my_list[i])
            i=i+1
    return new_list


















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)