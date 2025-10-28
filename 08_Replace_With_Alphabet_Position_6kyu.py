# Description:

# In this kata you are required to, given a string, replace every letter
# with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

# Example:
#   "The sunset sets at twelve o' clock."
#   "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


# Solution:
def alpha_pos(text):
    return " ".join(map(str,[ord(x.lower()) - 96 for x in text.replace(" ", "") if x.isalpha()]))


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(alpha_pos("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alpha_pos("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")


# Console command to make test work:
# python -m unittest 08_Replace_With_Alphabet_Position_6kyu -v