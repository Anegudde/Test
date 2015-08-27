import unittest


class TestClassA(unittest.TestCase):
    def testOne(self):
        # test code
        pass
    
if __name__ == '__main__':
    unittest.main(verbosity=1)
    print "completed TestA"    