# Micropython Calliopemini3 Motionkit2
# Fernsteuerung des Motionkit mit Infrarot
# Fernbedienung SEG KT-8000A
# 07/2025 Ch. Bijou

key_1          = 909
key_2          = 149
key_3          =  69
key_4          = 589
key_5          = 829
key_6          = 749
key_7          = 229
key_8          = 469
key_9          = 389
key_0          = 879 #dupl
key_prog       = 759 #dupl
key_clr        = 839
key_up         = 399
key_down       = 479
key_left       = 519
key_right      = 439
key_ok         = 269
key_display    = 119
key_audio      = 989
key_angle      = 669
key_subtitle   = 309
key_search     = 799 #dupl
key_openclose  = 279
key_title      = 799 #dupl
key_menue      = 839
key_return     = 239
key_setup      = 349
key_mode       = 999
key_volplus    = 639
key_volminus   = 759 #dupl
key_frwd       =  39
key_stop       = 919 #dupl
key_mute       = 679
key_ab         = 719
key_ffwd       = 959 #dupl
key_pausestep  = 879 #dupl
key_mark       = 599 
key_slowr      =  79
key_skipminus  = 959 #dupl
key_play       = 919 #dupl
key_zoom       = 109
key_slowf      = 159
key_skipplus   = 319







from microbit import *
import mklib as bot
import utime
import music

def nach_vorn():
    global tempo
    bot.motorR(0,tempo)
    bot.motorL(0,tempo)

def nach_rechts():
    global tempo
    bot.motorR(1,40)
    bot.motorL(0,40)

def nach_links():
    global tempo
    bot.motorR(0,40)
    bot.motorL(1,40)

def nach_hinten():
    global tempo
    bot.motorR(1,tempo)
    bot.motorL(1,tempo)

def halt():
    bot.motorR(0,0)
    bot.motorL(0,0)

def schneller():
    global tempo
    if tempo+10 < 255: tempo = tempo + 10

def langsamer():
    global tempo
    if tempo-10 > 0: tempo = tempo - 10

tempo = 100
while True:
#    utime.sleep_ms(500)
    cmd = bot.read_infrared()
#    print(cmd)
    if   cmd == key_up:       nach_vorn()
    elif cmd == key_down:     nach_hinten()
    elif cmd == key_right:    nach_rechts()
    elif cmd == key_left:     nach_links()
    elif cmd == key_ok:       halt()
    elif cmd == key_volplus:  schneller()
    elif cmd == key_volminus: langsamer()
    elif cmd == key_play:     music.play(music.NYAN)
    else: halt()
    
#FIN
