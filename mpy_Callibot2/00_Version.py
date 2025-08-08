# Micropython
# CalliopeV3 
# Callibot 2E
# 08/2025 Ch. Bijou

from microbit import *

i2c.init()
info=bytearray(10)
info[0] = 0x82

i2c.write(0x22, info)
info=i2c.read(0x22,10)

print(info)
   
print("Typ:      ",hex(info[1]))
print("Firmware: ",hex(info[5]), hex(info[4]), hex(info[3]), hex(info[2]))
print("SerienNr: ",hex(info[6]), hex(info[7]), hex(info[8]), hex(info[9]))
