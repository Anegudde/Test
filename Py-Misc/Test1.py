print "Loading TestSuite1"
import unittest
class Test1(unittest.TestSuite):

    def testEqual(self):
        self.failUnlessEqual(1, 3-2)

    def testNotEqual(self):
        self.failIfEqual(2, 3-2)

if __name__ == '__main__':
    print "completed Test1"
    unittest.main(verbosity=1)

