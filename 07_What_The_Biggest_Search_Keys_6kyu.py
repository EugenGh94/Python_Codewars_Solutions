# Description:

# You're a programmer in a SEO company. The SEO specialist of your company
# gets the list of all project keywords everyday, then he looks for the
# longest keys to analyze them.
# You will get the list with keywords and must write a simple function
# that returns the biggest search keywords and sorts them in lexicographical
# order.

# Examples:
#   'key1', 'key2', 'key n', 'bigkey2', 'bigkey1' -- "'bigkey1', 'bigkey2'"


# Solution:
def biggest_keys(*args):
    if len(args) == 0:
        return "''"
    else:    
        u = []
        for v in args:
            if len(v) == len(max(args, key=len)):
                u.append("'"+str(v)+"'")
        u.sort()
        return ', '.join(map(str, u))


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(biggest_keys("key1", "key22", "key333"), "'key333'")
        self.assertEqual(biggest_keys("coding", "sorting", "tryruby"), "'sorting', 'tryruby'")
        self.assertEqual(biggest_keys("small keyword", "how to coding?", "very nice kata", "a lot of keys", "I like Ruby!!!"), "'I like Ruby!!!', 'how to coding?', 'very nice kata'")
        self.assertEqual(biggest_keys("pippi"), "'pippi'")
        self.assertEqual(biggest_keys(), "''")


# Console command to make test work:
# python -m unittest 07_What_The_Biggest_Search_Keys_6kyu -v