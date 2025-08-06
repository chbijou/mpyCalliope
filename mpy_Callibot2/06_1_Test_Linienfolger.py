from microbit import *
import utime

i2c.init
while True:
    puffer = i2c.read(0x21, 1)
    print(puffer[0],hex(puffer[0]),puffer[0] & 0x0F)
    utime.sleep_ms(500)
          
      
      