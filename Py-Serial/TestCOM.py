import unittest
import sys, time
import serial

class ClassCOM (unittest.TestCase):
    def TestConnect(self):
            # close port
        print("Disconnecting")    

    def TestDisconnect(self):
        # test code
        pass
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print "completed TestA"    