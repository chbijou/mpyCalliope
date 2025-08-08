# Micropython Calliope mini3, Callibot 2E
# Ch. Bijou
# 08/2025

import cblib as bot
from microbit import *
import utime
# Front LED
for i in range(2):
    bot.ledR(1)           # rechts = Steuerbord
    utime.sleep_ms(500)
    bot.ledR(0)
    utime.sleep_ms(500)
   
    bot.ledL(1)           # links = Backbord
    utime.sleep_ms(500)
    bot.ledL(0)
    utime.sleep_ms(500)

    bot.ledR(1); bot.ledL(1)  # rechts + links
    utime.sleep_ms(500)
    bot.ledR(0); bot.ledL(0)
    utime.sleep_ms(500)
    
#RGB LED Unterseit
for i in range(2):
    bot.rgbled(16,0,0)
    utime.sleep_ms(1000)    
    bot.rgbled(0,16,0)
    utime.sleep_ms(1000)
    bot.rgbled(0,0,16)    
    utime.sleep_ms(1000)
    bot.rgbled(16,16,16)
    utime.sleep_ms(1000)
    bot.rgbled(0,0,0)
    utime.sleep_ms(1000)

# Spezialfunktion Callibot
for i in range(12):
    bot.CBrgbled("LV",15,0,0)
    utime.sleep_ms(100)
    bot.rgbled(0,0,0)
    bot.CBrgbled("RV",15,0,0)
    utime.sleep_ms(100)
    bot.rgbled(0,0,0)
    bot.CBrgbled("RH",15,0,0)
    utime.sleep_ms(100)
    bot.rgbled(0,0,0)
    bot.CBrgbled("LH",15,0,0)
    utime.sleep_ms(100)
    bot.rgbled(0,0,0)
           
# FIN
