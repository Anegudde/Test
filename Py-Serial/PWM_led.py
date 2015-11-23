#! /usr/bin/env python

import serial
import time
import usbtmc as tmc
from sys import exit

# output log
w=open('pwr_led_test.log', 'a')
if w.closed:
    print 'cannot open log'
    exit()

def log(s):
    w.write('{}\n'.format(s))
    print '{}'.format(s)

# set up serial connection
s=serial.Serial('/dev/ttyUSB0', 460800, timeout=0.1)

# set up meter
inst=tmc.instrument(tmc.AGILENT_34461A)
log('#'+inst.usb_info_string())
# reset multimeter
inst.write('*RST')
# request info
log('#ID: {}'.format(inst.ask('*IDN?')))
log('#Temp: {}'.format(inst.ask('SYST:TEMP?')))
log('#Uptime: {}'.format(inst.ask('SYST:UPT?')))
# switch to current mode
inst.write('CONF:CURR:DC 100 mA')
inst.write('CURR:DC:NPLC 100')
inst.write('TRIG:SOUR IMM')
inst.write('SAMP:COUN 3')

def inst_read():
    inst.write('INIT')
    while int(inst.ask('STAT:OPER:COND?'))&16:
        time.sleep(.4)
    resp=inst.ask('FETC?')
    return resp

# start synchronisation
s.flushInput()
char=''
while char=='':
    s.write('\x00')
    char=s.read(1)
if char!='\x00':
    log('bad sync return')
    exit()

def set_pwm(ch, val):
    # write command
    s.write('{}{}'.format(chr(ch), chr(val)))
    # check response
    if s.read(1)!=chr(ch):
        log('set_pwm ({},{}) bad response'.format(ch, val))
        exit()

# set outputs to zero
set_pwm(1,0)
set_pwm(2,0)
set_pwm(3,0)
set_pwm(4,0)

for i in range(0,256,15):
    set_pwm(1,i)
    log('{}\t{}'.format(i,inst_read().replace(',', '\t')))
for i in range(15,256,15):
    set_pwm(2,i)
    log('{}\t{}'.format(i+255,inst_read().replace(',', '\t')))
for i in range(15,256,15):
    set_pwm(3,i)
    log('{}\t{}'.format(i+510,inst_read().replace(',', '\t')))
for i in range(15,256,15):
    set_pwm(4,i)
    log('{}\t{}'.format(i+765,inst_read().replace(',', '\t')))
