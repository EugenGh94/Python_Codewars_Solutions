# Description:

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of
# 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If a number is a multiple of both 3 and 5, only count it once.


# Solution:
def solution(number):
    aaa = list(range(number))
    sum = 0

    if number > 0:
        for nr in aaa:
            if nr % 3 == 0 or nr % 5 == 0:
                sum = sum + nr
    else:    
        pass
    return sum


# Simple Tests:
import unittest
class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(solution(4), 3)
        self.assertEqual(solution(6), 8)
        self.assertEqual(solution(16), 60)
        self.assertEqual(solution(3), 0)
        self.assertEqual(solution(5), 3)
        self.assertEqual(solution(15), 45)
        self.assertEqual(solution(0), 0)
        self.assertEqual(solution(-1), 0)
        self.assertEqual(solution(10), 23)
        self.assertEqual(solution(20), 78)
        self.assertEqual(solution(200), 9168)


# Console command to make test work:
# python -m unittest 03_Multiples_of_3_or_5_6kyu -v