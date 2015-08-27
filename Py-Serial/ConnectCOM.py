import serial, time
import unittest

def Main():
    ser = serial.Serial(0,9600, parity='N',bytesize=8, stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)  # open first serial port
    print ser.name          # check which port was really used
    ser.write("US 1 1 1 \n")      # Connect to Device
    time.sleep(5)
    ser.close()             # close port
    print("Disconnecting")

def main():
    unittest.main()

if __name__ == '__main__':
    Main()


