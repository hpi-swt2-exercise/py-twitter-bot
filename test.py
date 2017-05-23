# https://docs.python.org/2/library/unittest.html
import unittest

from tweet_text import idle_text

# The basic building blocks of unit testing are test cases
# single scenarios that must be set up and checked for correctness.
# In unittest, test cases are represented by instances of unittest's TestCase class.
# To make your own test cases you must write subclasses of TestCase.


class TestTweetText(unittest.TestCase):

    def test_idle(self):
        # In order to test something, we use one of the assert*()
        # methods provided by the TestCase base class
        # https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertTrue
        self.assertTrue( isinstance(idle_text(), str) )



#if __name__ == '__main__':
#    unittest.main(verbosity=2)
