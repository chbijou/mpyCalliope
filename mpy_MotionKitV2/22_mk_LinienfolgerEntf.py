# Micropython Calliope
# Motionkit 2
# Linienfolger
# Herby 07/2025
# Erweiterung : Stop bei Annäherung

from microbit import *
import mklib as bot
import utime
import music

tempo_normal  = 60
tempo_langsam = 15
tempo_schnell = 80
richtung      = 99 # 0: vorwaerts, 1: rechts, 2: links
run_flag      = 0  # 0: stop, 1: run
abstand       = 10 # kritischer Abstand 

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
    bot.rgbLed(0,0,0)
    bot.ledR(1); bot.ledL(1)
    bot.motorR(0,tempo_normal)
    bot.motorL(0,tempo_normal)
    
def nach_rechts():
    bot.rgbLed(0,0,0)
    bot.ledR(1); bot.ledL(0)
    bot.motorR(0,tempo_langsam)
    bot.motorL(0,tempo_schnell)
    
def nach_links():
    bot.rgbLed(0,0,0)
    bot.ledR(0); bot.ledL(1)
    bot.motorR(0,tempo_langsam)
    bot.motorL(0,tempo_schnell)

def halt():
    bot.rgbLed(0,0,0)
    bot.ledR(0); bot.ledL(0)
    bot.motorR(0,0)
    bot.motorL(0,0)
              
def lauf():
    global richtung
    spur = bot.black_line() 
    display.show(spur)
    if   spur == 3:      # 3: mitte
         richtung = 0
         nach_vorn()
    elif spur == 1:      # 1: rechts aussen
         richtung= 1
         nach_links()
    elif spur == 2:      # 2: links aussen
         richtung = 2
         nach_rechts()   
    elif spur == 0 and richtung == 0: # 0: ganz aussen
         nach_vorn()

    elif spur == 0 and richtung == 1: # scharf nach links
         bot.rgbLed(120,0,0)           # rote Sonderbeleuchtung
         bot.ledR(0); bot.ledL(1)       # rote Frontleuchte
         bot.motorR(0,tempo_schnell)   # rechter Motor schnell
         bot.motorL(0,tempo_langsam)   # linker Motor langsam

    elif spur == 0 and richtung == 2: # scharf nach rechts
         bot.rgbLed(0,120,0)           # gruene Sonderbeleuchtung
         bot.ledR(1); bot.ledL(0)       # gruene Frontleuchte
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
         
    
