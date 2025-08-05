# Micropython
# CalliopeV3 Calli:bot2
# Entfernungsmesser
# 08/2025 Ch. Bijou
# Testumgebung: thonny

import cblib as bot 
from microbit import *
import utime

for i in range(20):
    dist=bot.read_ultraschall()
    print("Entfernung=",dist,"cm")
    utime.sleep_ms(1000)
    
# FIN
