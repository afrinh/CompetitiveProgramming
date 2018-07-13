import unittest


def get_permutations(string):
    length = len(string)
    list1 = list(string)
    if (string == ''):
        return set([string])
    set1 = set()
    permute(list1, 0, length - 1, set1)
    return set1

    # Generate all permutations of the input string
    


def permute(a, l, r,set1):
    if l==r:
        set1.add(toString(a))
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r,set1)
            a[l], a[i] = a[i], a[l]
            
def toString(List):
    return ''.join(List)
















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)