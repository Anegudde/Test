import visa
import time
import sys
import unittest
#import xlrd
#from HTMLReport import HTMLTestRunner

AGILENT_33220A= "USB0::0x0957::0x0407::MY44021621::0::INSTR" # - for 33220A
AGILENT_33522A= "USB0::0x0957::0x2307::MY50003961::0::INSTR" # - for 33522A

class TestSCPI() :  #unittest.TestCase):
    
    
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    @classmethod
    def List_Values(self):
        try:
            rm = visa.ResourceManager()
            rm.list_resources()    
            list_dev = visa.ResourceManager()
            inst_33522A= list_dev.open_resource(AGILENT_33522A)
            # Disable Output
            print(inst_33522A.write(":OUTP1:STAT 0"))
            print(inst_33522A.write(":OUTP2:STAT 0")) 
            print(inst_33522A.write(":SOUR1:FREQ:CW 1.1512 MHZ"))
            print(inst_33522A.write(":SOUR1:VOLT:LEV:IMM:AMPL 0.1"))
            print(inst_33522A.write(":SOUR1:BURS:PHAS 0 DEG"))
            print(inst_33522A.write(":OUTP1:LOAD 50"))
            print(inst_33522A.write(":SOUR1:BURS:PHAS 0 DEG"))
            print(inst_33522A.write(":SOUR1:BURS:INT:PER 0.1 S"))
            cw_freqy = float((inst_33522A.query(":SOUR1:FREQ?")))      
            print "Frequency is Set to:    ", cw_freqy #+ " Hertz"
            cw_amp = float(inst_33522A.query(':SOUR:VOLT:LEV:IMM:AMPL?'))
            print "Sample Rate:    ", cw_amp #+ " Volts"
            cw_bursttime = float(inst_33522A.query(":SOUR:BURS:NCYC?"))
            print "Burst Cycles:    ", cw_bursttime 
            output_impedance = float(inst_33522A.query(":OUTP1:LOAD?"))
            print "Output Impedance:    ", output_impedance #+ " Ohms"
            burst_phase = float(inst_33522A.query(":SOUR:BURS:PHAS?"))
            print "Burst Phase:    ", burst_phase  #+ " Degrees"
            burst_period = float(inst_33522A.query(":SOUR:BURS:INT:PER?"))
            print "Burst Period:    ", burst_period #+ " seconds"
            # Enable Output
            print(inst_33522A.write(":OUTP1:STAT 1"))
            print(inst_33522A.write(":OUTP2:STAT 0"))            
        #Fail Gracefully
        except IOError:
            print 'cannot Connect to Device: '+ AGILENT_33220A
        except Exception as e:
            print 'cannot Find the Device: '+ AGILENT_33220A
        else:
            print "Connection has been Closed"

        
    @classmethod
    def List_Device(self):
        try:
            rm = visa.ResourceManager()
            rm.list_resources()    
            list_dev = visa.ResourceManager()
            uSBDev= list_dev.open_resource(AGILENT_33522A)
            print(uSBDev.query("*IDN?", delay=1))
                #Fail Gracefully
        except IOError:
            print 'cannot Connect to Device: '+ AGILENT_33220A
        except Exception as e:
            print 'cannot Find the Device: '+ AGILENT_33220A
        else:
            print "Connection has been Closed"


if __name__ == "__main__":
    Test = TestSCPI()
    Test.List_Device()
    Test.List_Values()
    '''r
    print "completed Connecting to Device"   
    Test.List_Device()
    print "completed Testing Values for Device"   
    Test.List_Values()
    suite = unittest.TestSuite()   # (verbosity=2)
    suite.addTest(unittest.makeSuite(TestSCPI))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    buf = file("Test_Report" + "_" + dateTimeStamp + ".html", 'wb')
    runner = HTMLTestRunner(stream=buf,title='UnitTest Serial Port',description='Result of tests')
    runner.run(suite)
    '''

'''
# Get instrument VISAname
visaInstrList = visa.get_instruments_list()
myScope = visaInstrList[0]+'::INSTR'
scope = visa.instrument(myScope)
'''
#USB0::0x0957::0x2307::MY50003961::0::INSTR      - 33522A
#USB0::0x0957::0x0407::MY44021621::0::INSTR      - 33220A
