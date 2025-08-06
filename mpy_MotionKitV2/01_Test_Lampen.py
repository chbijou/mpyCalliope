# Micropython
# CalliopeV3 MotionKitV2
# LampenTest Front led und RGB_led
# 07/2025 Ch. Bijou

import mklib as bot
from microbit import *
import utime

for i in range(2):
    bot.ledR(1)           # rechts = Steuerbord
    utime.sleep_ms(500)
    bot.ledR(0)
    utime.sleep_ms(500)
   
    bot.ledL(1)           # links = Backbord
    utime.sleep_ms(500)
    bot.ledL(0)
    utime.sleep_ms(500)

    bot.ledB(1)           # rechts + links
    utime.sleep_ms(500)
    bot.ledB(0)
    utime.sleep_ms(500)

for i in range(2):
    
    bot.rgbled(255,0,0)
    utime.sleep_ms(1000)    
    bot.rgbled(0,255,0)
    utime.sleep_ms(1000)
    bot.rgbled(0,0,255)    
    utime.sleep_ms(1000)
    bot.rgbled(255,255,255)
    utime.sleep_ms(1000)
    bot.rgbled(0,0,0)
    utime.sleep_ms(1000)

# FIN
