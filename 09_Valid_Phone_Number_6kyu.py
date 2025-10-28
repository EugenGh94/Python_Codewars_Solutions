# Description:

# Write a function that accepts a string, and returns true if it is in
# the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a
# valid phone number.
# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)

# Examples:
#   "(123) 456-7890"  => true
#   "(1111)555 2345"  => false
#   "(098) 123 4567"  => false


# Solution:
def val_ph_no(phone_number):
    return (True if phone_number[1:4].isnumeric() and phone_number[6:9].isnumeric() and phone_number[10:14].isnumeric() and len(phone_number) == 14 and ''.join([phone_number[i] for i in [0,4,5,9]]) == "() -" else False)


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(val_ph_no("(123) 456-7890"),       True)
        self.assertEqual(val_ph_no("(1111)555 2345"),       False)
        self.assertEqual(val_ph_no("(098) 123 4567"),       False)
        self.assertEqual(val_ph_no("(123)456-7890"),        False)
        self.assertEqual(val_ph_no("abc(123)456-7890"),     False)
        self.assertEqual(val_ph_no("(123)456-7890abc"),     False)
        self.assertEqual(val_ph_no("abc(123)456-7890abc"),  False)
        self.assertEqual(val_ph_no("abc(123) 456-7890"),    False)
        self.assertEqual(val_ph_no("(123) 456-7890abc"),    False)
        self.assertEqual(val_ph_no("abc(123) 456-7890abc"), False)
        self.assertEqual(val_ph_no("(333) 185-0594"),       True)


# Console command to make test work:
# python -m unittest 09_Valid_Phone_Number_6kyu -v