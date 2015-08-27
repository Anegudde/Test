import unittest
import sys, time
import serial

class ClassCOM2 (unittest.TestCase):
    
    ser = serial.Serial(0,9600, parity='N',
                        bytesize=8, stopbits=1, timeout=None, 
                        xonxoff=False, rtscts=False, dsrdtr=False)  
    
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def testConnect(self):        
        print self.ser.name          # check which port was really used
    
    #@unittest.expectedFailure
    def testSend(self):
        if self.ser.isOpen():
            try:                
                self.ser.write("US 1 1 1 \n")      # Connect to Device
                time.sleep(3)
                pass
            except Exception, e1:
                print "error communicating...: " + str(e1)
                self.fail("Error Seen")
        else:    
            print "cannot open serial port "
            self.fail("Error Seen")
            self.ser.close() 
    
    def testReceive(self):
        pass
    
    def testDisconnect(self):
        self.ser.close()
             
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print "completed TestA"    