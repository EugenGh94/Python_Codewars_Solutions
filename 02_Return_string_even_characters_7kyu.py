# Description:

# Write a function that returns a sequence (index begins with 1) of all
# the even characters from a string. If the string is smaller than two
# characters or longer than 100 characters, the function should return
# "invalid string".

# For example:
#   "abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
#   "a"             --> "invalid string"


# Solution:
def even_chars(st): 
    try:
        w = []
        if len(st) >= 2 and len(st) <= 100:
            for i in range(len(st)):
                if (i+1) % 2 == 0:
                    w += st[i]
            return w
        else:
            return 'invalid string'
    except:
        return 'invalid string'


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(even_chars("a"), "invalid string")
        self.assertEqual(even_chars("abcdefghijklm"), ["b", "d", "f", "h", "j", "l"])
        self.assertEqual(even_chars("aBc_e9g*i-k$m"), ["B", "_", "9", "*", "-", "$"])


# Console command to make test work:
# python -m unittest 02_Return_string_even_characters_7kyu -v