import unittest

from TestClassA import TestClassA
from TestClassB import TestClassB

class AllTests(unittest.TestCase):
    def suite(self):
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TestClassA)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(TestClassB)
        return unittest.TestSuite([suite1, suite2])

def main():
    unittest.main()

if __name__ == '__main__':
    main()