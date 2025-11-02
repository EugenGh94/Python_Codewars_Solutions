# Description:

# ROT13 is a simple letter substitution cipher that replaces a letter
# with the letter 13 letters after it in the alphabet. ROT13 is an
# example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered
# with Rot13. If there are numbers or special characters included in
# the string, they should be returned as they are. Only letters from
# the latin/english alphabet should be shifted, like in the original
# Rot13 "implementation".
# Please note that using encode is considered cheating.


# Solution:
def rot13(m):
    return ''.join( chr((ord(n)+13-97)%26+97) if n.islower() else chr((ord(n)+13-65)%26+65) if n.isalpha() else n for n in m )


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(rot13('test'), 'grfg')
        self.assertEqual(rot13('Test'), 'Grfg')
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%')


# Console command to make test work:
# python -m unittest 11_Rot13_5kyu -v