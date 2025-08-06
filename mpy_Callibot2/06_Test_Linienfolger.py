# Micropython
# CalliopeV3 Calliobot2
# Linienfolger
# Test auf Prüfstand mit Teststreifen
# 07/2025 Ch. Bijou

import cblib as bot
from microbit import *
import utime
    
while True:
#    print("R:",bot.read_lineFollowR())
#    print("L:",bot.read_lineFollowL())
    display.show(bot.black_line()) 
#    bot.ledR(bot.read_lineFollowR())
#    bot.ledL(bot.read_lineFollowL())
    utime.sleep_ms(100)
    
# FIN
