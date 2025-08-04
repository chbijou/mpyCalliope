# Micropython Calliope mini 3
# dump i2c device mit adr = i2c_adresse
# n Zeilen a 16 Byte
# Herby 12/2020
# 07/2025 für Calliope mit Motionkit
# i2c.read(adr,puffer)

from microbit import *

# init
i2c.init()

def i2cdump(i2c_adr,zeile):
    puffer=i2c.read(i2c_adr,256)
    print('   ', end=' ')
    for i in range(16):
        print( '%3.1X'% (i), end=' ')
    print(' ')
    for j in range(zeile):
        print( '%3.2X'% (j), end=':')
        for i in range(16):
            res = puffer[j*16+i]
            print( '%3.2X'%  (res), end=' ')
        print(' ')
#   print(puffer)
i2cdump(0x10,4)

