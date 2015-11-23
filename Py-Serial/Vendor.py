#!/usr/bin/python
import sys
import usb.core
import visa
from time import sleep
#from pyvisa.shell import VisaShell

class TestGPIBUSB(object):
    pass
    
    @classmethod    
    def List_Resources(self):
        rm= visa.ResourceManager()
        rm.list_resources()
        try:
            rm.list_resources("*IDN?")
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    
    def test_List_Vendor(self):        
        dev = usb.core.find(find_all=True)
        # loop through devices, printing vendor and product ids in decimal and hex
        for cfg in dev:
            sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) +' & ProductID=' + str(cfg.idProduct) + '\n')
            sys.stdout.write('Hexadecimal: VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
    
    def TestGPIBUSB(self):
        rm = visa.ResourceManager()
        rm.list_resources()
        inst = rm.open_resource('USB0::0x0957::0x2307::MY50003961::0::INSTR')
        print(inst.query("*IDN?"))
        # "USB0::0x0957::0x2307::MY50003961::0::INSTR"

if __name__ == "__main__":
    c= TestGPIBUSB()
    c.TestGPIBUSB()
    
''' 
#USB0::0x0957::0x2307::MY50003961::0::INSTR      - for 33522A
#USB0::0x0957::0x0407::MY44021621::0::INSTR      - for 33220A
'''    
    
