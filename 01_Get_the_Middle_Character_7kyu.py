# Description:

# You are going to be given a non-empty string. Your job is to return the
# middle character(s) of the string.
#   If the string's length is odd, return the middle character.
#   If the string's length is even, return the middle 2 characters.

# Examples:
#   "test" --> "es"
#   "testing" --> "t"
#   "middle" --> "dd"
#   "A" --> "A"


# Solution:
def get_middle(s):
    return (s[(int(len(s)/2)-1):(int(len(s)/2)+1)] if len(s) % 2 == 0 else s[int(len(s)/2)])


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(get_middle("test"),"es")
        self.assertEqual(get_middle("testing"),"t")
        self.assertEqual(get_middle("middle"),"dd")
        self.assertEqual(get_middle("A"),"A")
        self.assertEqual(get_middle("of"),"of")


# Console command to make test work:
# python -m unittest 01_Get_the_Middle_Character_7kyu.py -v