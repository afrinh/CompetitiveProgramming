import unittest


def is_valid(code):

    # Determine if the input code is valid
    stack = []
    for bracket in code:
        if bracket == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif bracket == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
        elif bracket == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif bracket == '(' or bracket == '{' or bracket == '[':
            stack.append(bracket)
    return len(stack) == 0

    return False


















# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)