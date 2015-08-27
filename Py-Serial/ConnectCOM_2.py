import serial
import unittest
import time, os
from HtmlTestRun import HTMLTestRunner

class TestMethod1(unittest.TestCase):
    def Testsubmethod(self):
        print ("Inside TestMethod1:  testsubMethod")
        print self.ser.name          
        self.ser.write("US 1 1 1 \n")      
        time.sleep(5)
        pass

class serialPort():

    @classmethod
    def setUpModule(self):
        self.ser = serial.Serial(0,9600, parity='N',bytesize=8, stopbits=1, 
                timeout=None, xonxoff=False, 
                rtscts=False, dsrdtr=False)  
        print self.ser.name      # check which port was really used
        
    @classmethod
    def tearDownModule(self):
        self.ser.close()           
        print("Disconnecting")
        
    
    @classmethod
    def Test_Com(self):
        print ("Inside Test_Com")
    

def main():
    #unittest.main()
    test_classes_to_run = [TestMethod1]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    FullSuite = unittest.TestSuite(suites_list)
    dir = os.getcwd()
    outfile = open(dir + "\COMPortReport.html", "w")
    runner = HTMLTestRunner(stream = outfile,title = 'COM Port',
                            description = 'COM Port test')
    results = runner.run(FullSuite)    
    
if __name__ == '__main__':
    main()
    
    