# Micropython
# CalliopeV3 Calliobot2
# Linienfolger
# Test auf Prüfstand mit Teststreifen
# 07/2025 Ch. Bijou

import cblib as bot
from microbit import *
import utime
# Spuranzeige
spur_la =  Image("96666:" # links aussen
                 "96666:"
                 "96666:"
                 "96666:"
                 "96666")
spur_ra =  Image("66669:" # rechts aussen
                 "66669:"
                 "66669:"
                 "66669:"
                 "66669")
spur_mi =  Image("66966:" # mittig
                 "66966:"
                 "66966:"
                 "66966:"
                 "66966")
spur_ga =  Image("66666:" # ganz  aussen
                 "66666:"
                 "66666:"
                 "66666:"
                 "66666")    
while True:
    spur=bot.black_line()
#   print(spur)
    if   spur == 3: display.show(spur_ga)
    elif spur == 1: display.show(spur_ra)
    elif spur == 2: display.show(spur_la)
    elif spur == 0: display.show(spur_mi)
    else: pass
    utime.sleep_ms(100)
    
# FIN
