# Micropython
# CalliopeV3 MotionKitV2
# Linienfolger
# Test auf Prüfstand mit Teststreifen
# Herby 07/2025
# 

import mklib as bot
from microbit import *
import utime

    
while True:
#   print("R:",bot.read_lineFollowR())
#   print("L:",bot.read_lineFollowL())
    
    bot.black_line()
    bot.ledR(bot.read_lineFollowR())
    bot.ledL(bot.read_lineFollowL())
    utime.sleep_ms(100)
    
# FIN
