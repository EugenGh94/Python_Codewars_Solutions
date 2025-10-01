# Description:

# Complete the solution so that it splits the string into pairs of two
# characters. If the string contains an odd number of characters then
# it should replace the missing second character of the final pair with
# an underscore ('_').

# Examples:
#   'abc' =>  ['ab', 'c_']
#   'abcdef' => ['ab', 'cd', 'ef']


# Solution:
def solution(s):
    n = []
    for i in range(0, len(s), 2):
        if len(s) % 2 == 1:
            s = s + '_'
        n.append(s[i:i+2])
    return n


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
        self.assertEqual(solution("asdfads"), ['as', 'df', 'ad', 's_'])
        self.assertEqual(solution(""), [])
        self.assertEqual(solution("x"), ["x_"])


# Console command to make test work:
# python -m unittest 05_Split_Strings_6kyu -v