# unittest:
import unittest

addtwo = lambda x: x + 2

class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)

    def test_add_three(self):
        self.assertEqual(addtwo(3), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)

# doctest:
import  doctest

addtwo = lambda x: x + 2
addtwo.__doc__= """Add 2 to a number.
                >>> addtwo(2)
                4
                >>> addtwo(2.2)
                4.2
                >>> addtwo(3) #Should fail
                6
                """

if __name__ == '__main__':
    doctest.testmod(verbose=True)

