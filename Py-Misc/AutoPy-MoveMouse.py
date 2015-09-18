#!/usr/bin/env python
 
from autopy import key
from time import sleep
from jabbapylib.mouse import mouse
from jabbapylib.clipboard.clipboard import text_to_clipboards
#https://ubuntuincident.wordpress.com/tag/autopy/
TITLE = (68, 124)    # input text field's position
ADD = (575, 123)     # button's position
 
def delete():
    mouse.click_to(TITLE)
    key.tap('a', key.MOD_CONTROL)    # Ctrl+A
    key.tap(key.K_DELETE)            # Del
    sleep(.1)
 
def paste():
    mouse.click_to(TITLE)
    key.tap('v', key.MOD_CONTROL)    # Ctrl+V
    sleep(.1)
 
def add():
    mouse.click_to(ADD)
    sleep(.1)
 
def main():
    cnt = 0
    with open('movies.txt') as f:
        for title in f:
            title = title.rstrip('\n')
            text_to_clipboards(title)
 
            delete()
            paste()
            add()
            cnt += 1
 
    print cnt
 
#############################################################################
 
if __name__ == "__main__":
    print 'Switch to VirtualBox...'
    sleep(3)
    main()
