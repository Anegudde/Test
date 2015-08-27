import unittest

class TestClassB(unittest.TestCase):
    def testtwo(self):
        # test code
        print ("Class B:valid Value")
        pass
       
    @unittest.expectedFailure
    def testBtwo(self):
        # test code
        print ("Class B:TestbTwo")
        self.fail("Class B: Error Seen")
    
    def testBthree(self):
        # test code
        print ("Class B:TestBthree")
        pass
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print "completed TestB"   
    
  