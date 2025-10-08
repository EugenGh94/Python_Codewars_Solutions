# Description:

# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than
# one digit, continue reducing in this way until a single-digit number is
# produced. The input will be a non-negative integer.

# Examples:
#       16  -->  1 + 6 = 7
#      942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#   132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
#   493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


# Solution:
def digital_root(n):
    x = 0 
    while len(str(n)) > 1:
        for i in str(n):
            x += int(i)
        n = x
        x = 0
    return n


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(digital_root(16), 7, "digital_root(16)")
        self.assertEqual(digital_root(942), 6, "digital_root(942)")
        self.assertEqual(digital_root(132189), 6, "digital_root(132189)")
        self.assertEqual(digital_root(493193), 2, "digital_root(493193)")


# Console command to make test work:
# python -m unittest 06_Sum_of_Digits_Digital_Root_6kyu -v