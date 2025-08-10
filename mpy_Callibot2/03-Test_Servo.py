# Micropython
# Calliopemini3 Callibot2
# Servotest
# 07/2025 Ch.Bijou

import cblib as bot
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
    
