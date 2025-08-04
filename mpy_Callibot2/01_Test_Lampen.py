# Micropython
# CalliopeV3 MotionKitV2
# LampenTest Front LED und RGB_LED
# 07/2025 Ch. Bijou

import cblib as bot
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
    
    bot.rgbLed(16,0,0)
    utime.sleep_ms(1000)    
    bot.rgbLed(0,16,0)
    utime.sleep_ms(1000)
    bot.rgbLed(0,0,16)    
    utime.sleep_ms(1000)
    bot.rgbLed(16,16,16)
    utime.sleep_ms(1000)
    bot.rgbLed(0,0,0)
    utime.sleep_ms(1000)

# FIN
