from microbit import *
import utime

#Lesen Digitaleingaenge
dig = bytearray(1)
dig[0] =0x80
i2c.init()


while True:
    i2c.write(0x22,dig)
    dig=i2c.read(0x22,1) 
    dd = dig[0] & 0x03
    print(dd)
    utime.sleep_ms(100)