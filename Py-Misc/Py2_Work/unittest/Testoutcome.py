import unittest
import time, os
from HtmlTestRun import HTMLTestRunner


from ExceptionTest import ExceptionTest
from FixtureTest import FixturesTest
'''
https://pymotw.com/2/unittest/index.html
'''
class OutcomesTest(unittest.TestCase):

    def testPass(self):
        return

    def testFail(self):
        self.failIf(True)

    def testError(self):
        raise RuntimeError('Test error!')


class TruthTest(unittest.TestCase):

    def testFailUnless(self):
        self.failUnless(True)

    def testAssertTrue(self):
        self.assertTrue(True)

    def testFailIf(self):
        self.failIf(False)

    def testAssertFalse(self):
        self.assertFalse(False)

class EqualityTest(unittest.TestCase):

    def testEqual(self):
        self.failUnlessEqual(1, 3-2)

    def testNotEqual(self):
        self.failIfEqual(2, 3-2)

class InequalityTest(unittest.TestCase):

    def testEqual(self):
        self.failIfEqual(1, 3-2)

    def testNotEqual(self):
        self.failUnlessEqual(2, 3-2)

class AlmostEqualTest(unittest.TestCase):

    def testNotAlmostEqual(self):
        self.failIfAlmostEqual(1.1, 3.3-2.0, places=1)

    def testAlmostEqual(self):
        self.failUnlessAlmostEqual(1.1, 3.3-2.0, places=0)


if __name__ == '__main__':    
    test_classes_to_run = [OutcomesTest, TruthTest,EqualityTest,InequalityTest,AlmostEqualTest, ExceptionTest,FixturesTest]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    FullSuite = unittest.TestSuite(suites_list)
    dir = os.getcwd()
    outfile = open(dir + "\UnitTest.html", "w")
    runner = HTMLTestRunner(stream = outfile,title = 'Test Unit test',description = 'Test')
    results = runner.run(FullSuite)    
