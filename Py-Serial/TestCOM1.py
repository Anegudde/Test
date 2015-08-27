import unittest
import sys, time
import serial

class ClassCOM (unittest.TestCase):
    
    ser = serial.Serial(0,9600, parity='N',
                        bytesize=8, stopbits=1, timeout=None, 
                        xonxoff=False, rtscts=False, dsrdtr=False)  
    
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def testConnect(self):        
        print self.ser.name          # check which port was really used
    
    @unittest.expectedFailure
    def testSend(self):
        self.ser.write("U    S 1 1 1 \n")      
        time.sleep(5)
        pass
    
    def testReceive(self):
        pass
    
    def testDisconnect(self):
        self.ser.close()             # close port
        print("Disconnecting")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print "completed TestA"    