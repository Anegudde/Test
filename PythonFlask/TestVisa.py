from __future__ import division, unicode_literals, print_function, absolute_import

import visa

def test_itc4():
    print("Test start")
    itc4 = visa.Instrument("COM2", term_chars=b"\r", timeout=5)
    itc4.write(b"V")
    print(itc4.read())
    print("Test end")
