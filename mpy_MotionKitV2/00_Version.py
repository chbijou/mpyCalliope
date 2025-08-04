# Micropython
# CalliopeV3 MotionKitV2
# Motionkit Version
# 07/2025 Ch. Bijou
#
from microbit import *

i2c.init()
i2c.write(0x10, bytearray([0x32]))
puffer=i2c.read(0x10,21)
# print(puffer,puffer[0],puffer[1:16])

print("MotionKit Version:",puffer[1:int(puffer[0])+1])
      
