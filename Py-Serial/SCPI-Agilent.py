###########################################
#          AGILENT   33600A               #  
#         Waveform  Generator             #  
#                                         #  
###########################################
#                                         #
###########################################  


import visa
import pyvisa
import time
import numpy as np
from matplotlib import pyplot as plt

#_________________Signal Generation ___________________#

FS = 50000000.0
Ts = 1/FS

###  5 us low , 8 us high , 2 us low, 4 us high ####
N1 = int((5*(10**(-6)))/Ts)
N2 = int((8*(10**(-6)))/Ts)
N3 = int((2*(10**(-6)))/Ts)
N4 = int((4*(10**(-6)))/Ts)

signal = []
for i in range(0,N1):
    signal.append(0)

for i in range(0,N2):
    signal.append(5)
    
for i in range(0,N3):
    signal.append(0)

for i in range(0,N4):
    signal.append(5)

numpoints = len(signal)

packet_len = len(signal)*Ts*1000000.0

x = np.linspace(0,packet_len,len(signal))
plt.plot(x,signal,color='green',linestyle='-',linewidth=4)
plt.ylim(-0.2,5.2)
plt.xlabel('Time(us)')
plt.ylabel('Voltage')
plt.grid(color='b', linewidth=1)
plt.title("Generated Signal")
plt.show()

f = open("signal.dat","w+")
for item in signal:
    f.write("%s\n" %item)

f.close()

#_____________________Load To AFG _______________________#

header = '#' + str(len(str(numpoints * 2))) + str(numpoints * 2)

## How to write list of samples "signal" in function generator to play arb waveform "signal" ##
## Or how to copy file "signal.dat" in internal memory of function generator ##


rm = visa.ResourceManager()
AFG = rm.open_resource('USB0::0x0957::0x4807::MY53300148::INSTR')
print AFG.query("*IDN?")

AFG.write("*RST")
AFG.write("OUTP ON")
AFG.write("OUTP:LOAD INF")
AFG.write("APPL:ARB 5e7,5")
AFG.write("SOUR:BURST ON")
AFG.write("TRIGger:SOURce BUS")

TRIGGER_SOFT = 1


while(TRIGGER_SOFT):
    time.sleep(5)
    AFG.write("TRIG")

   
