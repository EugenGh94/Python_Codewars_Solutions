# Description:

# Write a function that takes in a string of one or more words, and
# returns the same string, but with all words that have five or more
# letters reversed (Just like the name of this Kata). Strings passed
# in will consist of only letters and spaces. Spaces will be included
# only when more than one word is present.

# Examples:
#   "Hey fellow warriors"  --> "Hey wollef sroirraw" 
#   "This is a test        --> "This is a test" 
#   "This is another test" --> "This is rehtona test"


# Solution:
def spin_words(sentence):
    old_list = sentence.split()
    new_list = []
    
    for word in old_list:
        if len(word) >= 5:
            new_word = word[::-1]
            new_list.append(new_word)
        else:
            new_list.append(word)

    return ' '.join(new_list)


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("to"), "to")
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")


# Console command to make test work:
# python -m unittest 04_Stop_gninnipS_My_sdroW!_6kyu -v