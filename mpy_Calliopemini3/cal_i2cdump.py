# Micropython Calliope mini 3
# dump i2c device mit adr = i2c_adresse
# n Zeilen a 16 Byte
# 12/2020 Ch. Bijou 
# 07/2025 für Calliope mit Motionkit
# i2c.read(adr,puffer)

from microbit import *

# init
i2c.init()

def i2cdump(i2c_adr,zeilen):
    puffer=i2c.read(i2c_adr,256)
    # Mantisse anzeigen
    print('   ', end=' ')
    for i in range(16):
        print( '%3.1X'% (i), end=' ')
    print(' ')
    # Puffer dumpen
    for j in range(zeilen):
        print( '%3.2X'% (j), end=':')
        for i in range(16):
            res = puffer[j*16+i]
            print( '%3.2X'%  (res), end=' ')
        print(' ')


i2cdump(0x10,16)

