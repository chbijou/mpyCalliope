#Micropython Calliope mini3 Calli:bot2
# NEU I2C-Adresse = 0x22 und Register
# Ch. Bijou
# 08/2025

from microbit import*

i2c.init()
# ---------- Motoren -----------------
def motorL(dir, speed): # ok
    buf_motor = bytearray(4)
    buf_motor[0] = 0x02    # Motoren                              
    buf_motor[1] = 0x01    # Moror 1 - rechts
    buf_motor[2] = dir     #Richtung auswählen 0:vorwärts | 1:rückwärts
    buf_motor[3] = speed   # Geschwindigkeit von 0 - 255
    i2c.write(0x22, buf_motor)

def motorR(dir, speed): # ok
    buf_motor = bytearray(4)
    buf_motor[0] = 0x02    # Motoren                               
    buf_motor[1] = 0x02    # Moror 2 - links 
    buf_motor[2] = dir     #Richtung auswählen 0:vorwärts | 1:rückwärts
    buf_motor[3] = speed   # Geschwindigkeit von 0 - 255
    i2c.write(0x22, buf_motor)
              
#------------ LEDs --------------------------
def ledR(on_off): # Front LED rechts (gruen)
    buf_led = bytearray(5)
    buf_led[0] = 0x03   # LEDs steuern
    buf_led[1] = 0x06   # LED rechts
    if on_off == 1 : buf_led[2] = 0x0F # pwm 1-15
    else:            buf_led[2] = 0x00 # aus
    i2c.write(0x22, buf_led)
    
def ledL(on_off): # Front LED links (rot)
    buf_led = bytearray(5)
    buf_led[0] = 0x03   # LEDs steuern
    buf_led[1] = 0x05   # LED links
    if on_off == 1 : buf_led[2] = 0x0F # pwm 1-15
    else:            buf_led[2] = 0x00 # aus
    i2c.write(0x22, buf_led)
    
def rgbled(red, green, blue): # ok
    # Alle 4 RGB-LEDs gleichzeitig schalten
    # Prinzip MotionKit2
    buf_rgbled = bytearray(5)
    buf_rgbled[0] = 0x03
    for index in range(4):
        buf_rgbled[1] = index+1
        buf_rgbled[2] = red
        buf_rgbled[3] = green
        buf_rgbled[4] = blue
        i2c.write(0x22, buf_rgbled)

def CBrgbled(position,red, green, blue): # ok
    # Zusatzfunktion fuer Calli:bot2
    # Beim Calli:bot2 lassen sich die RGB leds einzeln ansteuern
    # Positionen sind "LV" "RV" "LH" "RH"
    buf_rgbled = bytearray(5)
    buf_rgbled[0] = 0x03
    if position   == "LV": buf_rgbled[1] = 1
    elif position == "LH": buf_rgbled[1] = 2
    elif position == "RH": buf_rgbled[1] = 3
    elif position == "RV": buf_rgbled[1] = 4
    buf_rgbled[2] = red
    buf_rgbled[3] = green
    buf_rgbled[4] = blue
    i2c.write(0x22, buf_rgbled)
    
# -------------------Servo ----------------
def servoS1(angle): # Test offen
    buf_servoS1 = bytearray(2)
    buf_servoS1[0] = 0x14   #Auswahl ServoS1
    buf_servoS1[1] = angle   #Winkel von 0 - 180
    i2c.write(0x10, buf_servoS1)

def servoS2(angle): # Test offen
    buf_servoS2 = bytearray(2)
    buf_servoS2[0] = 0x15   #Auswahl ServoS2
    buf_servoS2[1] = angle   #Winkel von 0 - 180
    i2c.write(0x10, buf_servoS2)
    
# --------- Linienfolger --------------
def black_line(): # ok
# 0: ganz ausserhalb
# 1: rechts ausserhalb
# 2: links ausserhalb
# 3: mitten auf der Spur
    dig = bytearray(1)
    dig[0] =0x80
    i2c.write(0x22,dig)
    dig=i2c.read(0x22,1)
    data = dig[0] & 0x03 #Spursucher bit 0: rechts; bit1: links
    if   data == 0x00: data = 0x03
    elif data == 0x03: data = 0x00
    return data

# ----------Ultraschall  / Entfernung -------
def read_ultraschall(): # ok
    buf=bytearray(3)
    buf[0] = 0x81
    i2c.write(0x22,buf)
    buf = i2c.read(0x22,3)
    return  int((buf[1] + 256 *buf[2]) / 10)
    
# FIN
