
MPY: soft reboot
MicroPython v1.23.0 on 2025-07-18; micro:bit v2.1.1 with nRF52833
Type "help()" for more information.
>>> from microbit import *
>>> i2c.scan()
[32, 33, 34, 35, 36, 37, 38, 39]
>>> 
32 0x20 0x00       Motor 0x00 links; 0x02 rechts 3 Bytes
        0x00       Richtung 0x00 vor; 0x01 rück
        0x00       Geschwindigkeit 0 - 255
        
33 0x21 0x00       Front-LED 2 Bytes
        0x00       on/off  Bitmuster

33 0x21 0x00       Linienfolger 1 Byte 0x80: mitte,
                                       0x81: rechts aussen
                                       0x82: links aussen
                                       0x83: ganz aussen
        
33 0x21 0x80       Entfernung 3 Bytes    
        0x00       dist High 0x00 - 0xFF
        0x00       dist Low  0x00 - 0xFF
        
34 0x22 0x03       RGB- LED  5 Bytes
        0x00       index 1:LV; 2:LH; 3:RH; 4:RV 
        0x00       rot   0x00 - 0xFF
        0x00       grün  0x00 - 0xFF
        0x00       blau  0x00 - 0xFF
        