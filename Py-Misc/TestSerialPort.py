from HtmlTestRun import HTMLTestRunner
import unittest, time
        
class TestSerialPort(unittest.TestCase):
    def setup(self):
        import serial
        ser = serial.Serial(0,115200, parity='N',bytesize=8, stopbits=1, 
                            timeout=None, xonxoff=False, 
                            rtscts=False, dsrdtr=False)  
                            # open first serial port
        print ser.name      # check which port was really used    
        try: 
            #ser.open()
            pass
        except Exception, e:
            print "error open serial port: " + str(e)
            exit()
        if ser.isOpen():
            try:                
                ser.write("US 1 1 1 \n")      # Connect to Device
                time.sleep(3)
                ser.write("US 1 2 130 \n")      # Send a Value
                assert 1
                time.sleep(3)
                ser.write("US 1 2 118 \n")      # Send a Value
                time.sleep(3)
                assert 1
                ser.write("US 1 2 162 \n")      # Send a Value
                time.sleep(3)
                assert 1
                ser.write("US 1 2 150 \n")      # Send a Value
                time.sleep(3)
                assert 1
                ser.write("US 1 1 0 \n")      # Disconnect COM
                print("Disconnecting")
                assert 1
                time.sleep(5)
                ser.close()
                print ("Closing the Ports")
                assert 1
            except Exception, e1:
                print "error communicating...: " + str(e1)
        else:    
            print "cannot open serial port "
            ser.close()            
        
            

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSerialPort))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    runner = HTMLTestRunner(stream=buf,title='Test Serial Port',description='Result of tests')
    runner.run(suite)
