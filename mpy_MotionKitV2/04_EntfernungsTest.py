# Micropython
# CalliopeV3 MotionKitV2
# Entfernungsmesser
# Herby 07/2025

import mklib as bot 
from microbit import *
import utime

for i in range(20):
    dist=bot.read_ultraschall()
    print("Entfernung=",dist,"cm")
    utime.sleep_ms(1000)
    
# FIN
