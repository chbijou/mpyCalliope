# Micropython
# CalliopeV3 MotionKitV2
# Infrarot Empfang
# Herby 07/2025
# Testmöglichkeiz z.Zt unbekannt
# Welchre IR-Quelle wierd verwendet?

import mklib as bot
from microbit import *
import utime

while True:
    empfang=bot.read_infrared()
    if empfang !=0: print(empfang)
    utime.sleep_ms(100)
    
# FIN
