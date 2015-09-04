import serial, time

def Main():
    ser = serial.Serial(0,115200, parity='N',bytesize=8, stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)  # open first serial port
    print ser.name          # check which port was really used
    ser.write("US 1 1 1 \n")      # Connect to Device
    time.sleep(31)
    ser.write("US 1 2 130 \n")      # Send a Value
    time.sleep(31)
    ser.write("US 1 2 118 \n")      # Send a Value
    time.sleep(31)
    ser.write("US 1 2 162 \n")      # Send a Value
    time.sleep(31)
    ser.write("US 1 2 150 \n")      # Send a Value
    time.sleep(31)
    ser.write("US 1 1 0 \n")      # Disconnect COM
    print("Disconnecting")
    time.sleep(15)
    