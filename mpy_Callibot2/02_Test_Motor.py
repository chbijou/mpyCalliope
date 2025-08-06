# Micropython
# CalliopeV3 Calli:bot2
# Motortest
# 07/2025 Ch. Bijou
# Testumgebung thonny

import cblib as bot
from microbit import *
import utime

tempo=255  # 0 - 255
for i in range(2):
    bot.ledR(1)
    bot.motorR(0,tempo)
    utime.sleep_ms(2000)
    bot.motorR(1,tempo)
    utime.sleep_ms(2000)
    bot.ledR(0)
    bot.motorR(0,0)
  
    bot.ledL(1)
    bot.motorL(0,tempo)
    utime.sleep_ms(2000)
    bot.motorL(1,tempo)
    utime.sleep_ms(2000)
    bot.ledL(0)
    bot.motorL(0,0)
    
#FIN    
    
