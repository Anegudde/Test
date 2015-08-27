import unittest, time
import serial
from HtmlTestRun import HTMLTestRunner
             
class TestSerialPort(unittest.TestCase):
    @classmethod
    def setUpModule():
        setup(self)
        
    @classmethod
    def tearDownModule():
        close()
    
    def setup(self):        
        ser = serial.Serial(0,115200, parity='N',bytesize=8, stopbits=1, 
                            timeout=None, xonxoff=False, 
                            rtscts=False, dsrdtr=False)  
        print ser.name      # check which port was really used
        pass
                
    def connect(self):    
        try: 
            self.ser.open()
            pass
        except Exception, e:
            raise RuntimeError("Error Reported in Connection")
            print "error open serial port: " + str(e)

    
    def sendCommand(self): 
        if self.ser.isOpen():
            try:                
                self.ser.write("US 1 1 1 \n")      # Connect to Device
                time.sleep(3)                
                self.ser.write("US 1 2 130 \n")      # Send a Value
                time.sleep(3)
                self.ser.write("US 1 2 118 \n")      # Send a Value
                time.sleep(3)
                self.ser.write("US 1 2 162 \n")      # Send a Value
                time.sleep(3)
                self.ser.write("US 1 2 150 \n")      # Send a Value
                time.sleep(3)
                self.ser.write("US 1 1 0 \n")      # Disconnect COM
                print("Disconnecting")
                time.sleep(5)
                self.ser.close()
                print ("Closing the Ports")
                pass
            except Exception, e1:
                print "error communicating...: " + str(e1)
                self.fail("Error Seen")
        else:    
            print "cannot open serial port "
            self.fail("Error Seen")
            self.ser.close()            
        
        def close(self):
            if self.ser.isOpen():
                self.ser.close() 
            
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSerialPort))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    runner = HTMLTestRunner(stream=buf,title='UnitTest Serial Port',description='Result of tests')
    runner.run(suite)
