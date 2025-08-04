# Micropython
# CalliopeV3 MotionKitV2
# Infrarot Empfang
# 07/2025 Ch. Bijou
# Test mit Fernbedienung SEG KT-8000A

import mklib as bot
from microbit import *
import utime

while True:
    empfang=bot.read_infrared()
    if empfang !=0: print(empfang)
    utime.sleep_ms(100)
    
# FIN
