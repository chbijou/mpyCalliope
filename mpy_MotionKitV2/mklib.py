# Module für Motionkit 2
# Quelle: github.com/tinysuperlab/MotionKit_MicroPython
# 08/2025 Ch. Bijou
# Vergl. cblib (für Callibot2) 
# letzte Aenderung:
# 2025.08.11. - Bereinungung

from microbit import*

#Initialisiere das MotionKit
i2c.init()

def motorL(dir, tempo):
    buf_motorL = bytearray(3)
    buf_motorL[0] = 0x00    # Motor auswählen - 0x00: Motor rechts
    buf_motorL[1] = dir     # Richtung auswählen 0:vorwärts | 1:rückwärts
    buf_motorL[2] = tempo   # Geschwindigkeit von 0 - 255
    i2c.write(0x10, buf_motorL)

def motorR(dir, tempo):
    buf_motorR = bytearray(3)
    buf_motorR[0] = 0x02    #Motor auswählen - 0x02: Motor links
    buf_motorR[1] = dir     #Richtung auswählen 0:vorwärts | 1:rückwärts
    buf_motorR[2] = tempo   #Geschwindigkeit von 0 - 255
    i2c.write(0x10, buf_motorR)

def ledR(on_off):
    # schalte rechte LED
    buf_ledR = bytearray(2)
    buf_ledR[0] = 0x0C     # rechte LED
    buf_ledR[1] = on_off   #LED 0:aus 1:an
    i2c.write(0x10, buf_ledR)

def ledL(on_off):
    # schalte linke LED
    buf_ledL = bytearray(2) 
    buf_ledL[0] = 0x0B     # Linke LED
    buf_ledL[1] = on_off   #LED 0:aus | 1:an
    i2c.write(0x10, buf_ledL)

def rgbled(red, green, blue):
    buf_rgbled_red = bytearray(2)
    buf_rgbled_red[0] = 0x18      #Auswahl rote LED
    buf_rgbled_red[1] = red       #Farbwert von 0 - 255
    buf_rgbled_green = bytearray(2)
    buf_rgbled_green[0] = 0x19    #Auswahl grüne LED
    buf_rgbled_green[1] = green   #Farbwert von 0 - 255
    buf_rgbled_blue = bytearray(2)
    buf_rgbled_blue[0] = 0x1A     #Auswahl blaue LED
    buf_rgbled_blue[1] = blue     #Farbwert von 0 - 255
    i2c.write(0x10, buf_rgbled_red)
    i2c.write(0x10, buf_rgbled_green)
    i2c.write(0x10, buf_rgbled_blue)

def servoS1(winkel):
    buf_servoS1 = bytearray(2)
    buf_servoS1[0] = 0x14     #Auswahl ServoS1
    buf_servoS1[1] = winkel   #Winkel von 0 - 180
    i2c.write(0x10, buf_servoS1)

def servoS2(winkel):
    buf_servoS2 = bytearray(2)
    buf_servoS2[0] = 0x15     #Auswahl ServoS2
    buf_servoS2[1] = winkel   #Winkel von 0 - 180
    i2c.write(0x10, buf_servoS2)

def black_line():
# 0: ganz ausserhalb
# 1: rechts ausserhalb
# 2: links ausserhalb
# 3_ mitten auf der Spur
    i2c.write(0x10,bytearray([0x1D]))
    sleep(20)
    data = i2c.read(0x10,1)[0]
    return(data)

def read_ultraschall():
    i2c.write(0x10, bytearray([0x28]))   #Trigger-Signal an den Ultraschallsensor
    sleep(20)
    data = i2c.read(0x10, 2)   #Auslesen des Signals
    distance = (data[0] << 8) | data[1]
    return distance

def read_infrared():
    i2c.write(0x10, bytearray([0x2B]))
    sleep(20)
    buf_ir = i2c.read(0x10, 4)   #Auslesen des Signals
    data = buf_ir[3] | (buf_ir[2] << 8) | (buf_ir[1] << 16) | (buf_ir[0] << 24)
    return data % 1000  # Reduziert die Zahl auf maximal drei Stellen

# FIN
