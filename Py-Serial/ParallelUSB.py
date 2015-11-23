#paperdraft_nigg_2015.pdf
# -*- coding: utf-8 -*-
import serial
from threading import Thread
from time import sleep

class PeriodicDMM(Thread):
	value=0

def init(self,device):
	self.com=serial.Serial(device,9600,timeout=1)
	nil=self.port.read(100)

def run(self):
	while True:
			res=self.port.read(10)
			self.value=float(res[0:6])
			sleep(0.8)

def getvalue(self):
	returnself.value
	
#--------------------------------	
import periodicdmm
dmm=periodicdmm.PeriodicDMM("/dev/ttyUSB0")
dmm.start()
print dmm.getvalue()


dmmA=slowdmm.SlowDMM("/dev/ttyUSB0")
dmmB=slowdmm.SlowDMM("/dev/ttyUSB1")
dmmC=slowdmm.SlowDMM("/dev/ttyUSB2")
#init()
dmmA.start()
dmmB.start()
dmmC.start()
while True:
	sleep(0.2)
	#saveRes(dmmA.get(),dmmB.get(),dmmC.get()
print "End"
	
#------------------
import ivi
from time import sleep
import myDUT
supvolt=[3.6,3.8,4.0,4.2,4.4]
drivcur=[0.002, 0.003, 0.003, 0.004, 0.005]#][ 20E−3, 30E−3, 40E−3, 50E−3]
speed=[100,200,400,800]
dmm=ivi.agilent.agilent34410A("TCPIP::10.1.1.2::INSTR")
dso=ivi.lecroy.lecroyWR62XIA("TCPIP::10.1.1.3::INSTR")
psu=ivi.agilent.agilentE3649A("TCPIP::10.1.1.4::INSTR")
dut=myDUT.init()
chan=range(4)
psu.outputs[0].voltagelevel=supvolt[0]
psu.outputs[0].enabled=True
for sv in supvolt:
	for dc in drivcur:
		for sp in speed:
			psu.outputs[0].voltagelevel=sv
			dut.set(driver=dc,speed=sp)
			print "Wait at%.1fV,%imA,%ikHz" %(sv,(dc*1000),sp)
			dut.starttx()
			sleep(55)
			dso.trigger.mode=single
			sysi=psu.outputs[0].getcurrent()
			syst=dmm.measurement.read(0)
			sleep(5)
			for c in range(4):
				chan[c]=dso.channels[c].measuremen.fetchwaveform()
				png=dso.display.fetchscreenshot()
				picname="run%.1fV%imA%ikHz.png"%(sv,(dc*1000),sp)
			f=open(picname,wb)
			f.write(png)
			f.close()
			procsave(sv,dc,sp,chan,sysi,syst)


#-------------------------------------            
#import ivi
#import time
dmm=ivi.agilent.agilent34410A("TCPIP::10.1.1.2::INSTR")
log=open("log.txt","a")
while True:
	log.write("%0.4f◦ C\n" %dmm.measurement.read(0))
	time.sleep(10)
print "End"
