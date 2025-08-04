# Micropython
# CalliopeV3 MotionKitV2
# Servotest
# Herby 07/2025

import mklib as bot
from microbit import *
import utime

for i in range(7):
    winkel=30*i
    bot.servoS1(winkel)
    utime.sleep_ms(1000)
bot.servoS1(0)

for i in range(7):
    winkel=30*i
    bot.servoS2(winkel)
    utime.sleep_ms(1000)
bot.servoS2(0)

#FIN    
    
