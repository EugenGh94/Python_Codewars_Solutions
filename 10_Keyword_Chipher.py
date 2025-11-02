# Description:

# Third day at your new cryptoanalyst job and you come across your
# toughest assignment yet. Your job is to implement a simple keyword
# cipher. A keyword cipher is a type of monoalphabetic substitution
# where two parameters are provided as such (string, keyword). The
# string is encrypted by taking the keyword, dropping any letters
# that appear more than once. The rest of the letters of the alphabet
# that aren't used are then appended to the end of the keyword.
# For example, if your string was "hello" and your keyword was "wednesday",
# your encryption key would be 'wednsaybcfghijklmopqrtuvxz'.

# To encrypt 'hello' you'd substitute as follows:
#              abcdefghijklmnopqrstuvwxyz
#  hello ==>   |||||||||||||||||||||||||| ==> bshhk
#              wednsaybcfghijklmopqrtuvxz


# Solution:
def keyword_cipher(msg, keyword):
    
    # Keyword manipulation
    j = [g for g in "".join(dict.fromkeys(("".join([e for e in keyword]) + "".join([chr(u) for u in range(97, 123)]))))]
    
    # Alphabet
    m = [chr(u) for u in range(97, 123)]
    
    # Main function
    new_msg = ''
    for i in msg.lower():
        if i.isalpha() == True:
            new_msg += j[m.index(i)]
        else:
            new_msg += i
    msg = new_msg
    
    return msg


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(keyword_cipher("Welcome home","secret"), "wticljt dljt")
        self.assertEqual(keyword_cipher("hello","wednesday"), "bshhk")
        self.assertEqual(keyword_cipher("HELLO","wednesday"), "bshhk")
        self.assertEqual(keyword_cipher("HeLlO","wednesday"), "bshhk")
        self.assertEqual(keyword_cipher("WELCOME HOME", "gridlocked"), "wlfimhl kmhl")
        self.assertEqual(keyword_cipher("alpha bravo charlie", "delta"), "djofd eqdvn lfdqjga")
        self.assertEqual(keyword_cipher("Home Base", "seven"), "dlja esqa")
        self.assertEqual(keyword_cipher("basecamp", "covert"), "ocprvcil")
        self.assertEqual(keyword_cipher("one two three", "rails"), "mks twm tdpss")
        self.assertEqual(keyword_cipher("Test", "unbuntu"), "raqr")


# Console command to make test work:
# python -m unittest 10_Keyword_Chipher -v