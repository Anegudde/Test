import unittest
import sys


class TestClassA(unittest.TestCase):
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def testOne(self):
        # test code
        print ("Class A:TestOne")
            
    
    @unittest.skip("demonstrating skipping")
    def testsix(self):
        # test code
        print ("Class A:TestSix")
        pass
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print "completed TestA"    
    
