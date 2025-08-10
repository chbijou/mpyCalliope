# Micropython Calliopemini3 Callibot2
# Versorgungsspannung auslesen
# i2c-Adresse 0x22 i2c-Register 0x83
# Ch. Bijou 08/2025

from microbit import *

i2c.init()
info=bytearray(3)
info[0] = 0x83

i2c.write(0x22, info)
info=i2c.read(0x22,3)

spannung  = int(info[1])  +  256 * int(info[2])
print("Versorgungsspannung",spannung/1000,"V")
   
