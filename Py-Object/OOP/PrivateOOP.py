#!/usr/bin/python
import unittest
from testtools.testcase import ExpectedException
from twisted.test.test_ftp import PrintLines
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
for i in range(1,10):
    counter.count()

print counter._JustCounter__secretCount

@unittest.expectedFailure
def Test_Private():
    print counter.__secretCount
    
if __name__ == "__main__":
    unittest.main(verbosity=2)