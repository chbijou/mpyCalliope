# Micropython Calliope
# Callibot
# Linienfolger
# 07/2025 Ch. Bijou
# Erweiterung : Stop bei Annäherung + Sound

from microbit import *
import cblib as bot
import utime
import music

tempo_normal  = 120
tempo_langsam = int(tempo_normal / 2)
tempo_schnell = int(tempo_normal * 2)
richtung      = 99 # 0: vorwaerts, 1: rechts, 2: links
run_flag      = 0  # 0: stop, 1: run
abstand       = 10 # kritischer Abstand 
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

pfeil_r =  Image("00900:"
                 "09009:"
                 "90090:"
                 "09009:"
                 "00900")

licht_aus = Image("00000:"
                  "00000:"
                  "00000:"
                  "00000:"
                  "00000")

def nach_vorn():
    bot.ledR(1); bot.ledL(1)
    bot.motorR(0,tempo_normal)
    bot.motorL(0,tempo_normal)
    
def nach_rechts():
    bot.ledR(1); bot.ledL(0)
    bot.motorR(0,tempo_langsam)
    bot.motorL(0,tempo_schnell)
    
def nach_links():
    bot.ledR(0); bot.ledL(1)
    bot.motorR(0,tempo_schnell)
    bot.motorL(0,tempo_langsam)

def halt():
    bot.ledR(0); bot.ledL(0)
    bot.motorR(0,0)
    bot.motorL(0,0)
              
def lauf():
    global richtung
    spur = bot.black_line() 
#    display.show(spur)
    if   spur == 3:      # 3: mitte
         display.show(spur_mi)
         richtung = 0
         nach_vorn()
    elif spur == 1:      # 1: rechts aussen
         display.show(spur_ra)
         richtung= 1
         nach_links()
    elif spur == 2:      # 2: links aussen
         display.show(spur_la)
         richtung = 2
         nach_rechts()
    elif spur == 0:      # ganz ausserhalb
         display.show(spur_ga)
         if   richtung == 0: richtung = 2
         elif richtung == 1:  # scharf nach links
              bot.ledR(0); bot.ledL(1)      # rote Frontleuchte
              bot.motorR(0,tempo_schnell)   # rechter Motor schnell
              bot.motorL(0,tempo_langsam)   # linker Motor langsam
         elif richtung == 2: # scharf nach rechts
              bot.ledR(1); bot.ledL(0)      # gruene Frontleuchte
              bot.motorR(0,tempo_langsam)   # rechter Motor langsam
              bot.motorL(0,tempo_schnell)   # linker Motor schnell

def start_bot():
     halt()
     while True:
         display.show(pfeil_r)
         if button_a.is_pressed():
            run_flag = 1
            display.show(licht_aus)
            break
              
start_bot()
while True:
    dist=bot.read_ultraschall()
    if dist > abstand: lauf()
    else:
        halt()
        for i in range(4):
            music.pitch(440, 100)
            music.pitch(880, 100)
        utime.sleep_ms(500)

# FIN         
