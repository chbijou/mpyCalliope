#Micropython Calliope mini3 Calli:bot2
#Vergl. mklib (für Motionkit2)

from microbit import*

#Initialisiere Callibot
i2c.init()

def motorL(dir, speed): #ok
    buf_motor1 = bytearray(3)
    buf_motor1[0] = 0x00    # Motor auswählen - 0x00: Motor links
    buf_motor1[1] = dir     # Richtung auswählen 0:vorwärts | 1:rückwärts
    buf_motor1[2] = speed   # Geschwindigkeit von 0 - 255
    i2c.write(0x20, buf_motor1)

def motorR(dir, speed): #ok
    buf_motor2 = bytearray(3)
    buf_motor2[0] = 0x02    #Motor auswählen - 0x02: Motor rechts
    buf_motor2[1] = dir     #Richtung auswählen 0:vorwärts | 1:rückwärts
    buf_motor2[2] = speed   #Geschwindigkeit von 0 - 255
    i2c.write(0x20, buf_motor2)

def ledR(on_off): #ok
    buf_led = bytearray(2)
    buf_led[0]=0
    if on_off == 1 : buf_led[1] |= 0x02
    else:            buf_led[1] &= 0xFD
    i2c.write(0x21, buf_led)
    
def ledL(on_off): #ok
    buf_led = bytearray(2) 
    buf_led[0] = 0
    if on_off == 1 : buf_led[1] |= 0x01
    else:            buf_led[1] &= 0xFE
    i2c.write(0x21, buf_led)

def ledB(on_off): # ok
    buf_led = bytearray(2)
    buf_led[0] = 0
    if on_off == 1 : buf_led[1] |= 0x03
    else:            buf_led[1] &= 0xFE
    i2c.write(0x21, buf_led)
    
def rgbled(red, green, blue): #ok
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

def CBrgbled(position,red, green, blue): #ok
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
    

def servoS1(angle):
    buf_servoS1 = bytearray(2)
    buf_servoS1[0] = 0x14   #Auswahl ServoS1
    buf_servoS1[1] = angle   #Winkel von 0 - 180
    i2c.write(0x10, buf_servoS1)

def servoS2(angle):
    buf_servoS2 = bytearray(2)
    buf_servoS2[0] = 0x15   #Auswahl ServoS2
    buf_servoS2[1] = angle   #Winkel von 0 - 180
    i2c.write(0x10, buf_servoS2)

def read_lineFollowR():
    i2c.write(0x10, bytearray([0x1D]))
    data = i2c.read(0x10, 1)[0]   #Auslesen des Sensors
    
    # Überprüfen, ob das Bit für den rechten Sensor gesetzt ist
    return 0 if (data & 0x01) != 0 else 1 

def read_lineFollowL():
    i2c.write(0x10, bytearray([0x1D]))  
    data = i2c.read(0x10, 1)[0]   #Auslesen des Sensors
    
    # Überprüfen, ob das Bit für den linken Sensor gesetzt ist
    return 0 if (data & 0x02) != 0 else 1

def black_line(): #ok
# 0: ganz ausserhalb
# 1: rechts ausserhalb
# 2: links ausserhalb
# 3_ mitten auf der Spur
    data = i2c.read(0x21,1)[0]
    # etwas anders als bei MotionKit2
    data = data & 0x0F
    if   data == 0: data = 3
    elif data == 3: data = 0
    return(data)

def read_ultraschall(): #ok
    buf = i2c.read(0x21,3)
    return  int((256 * buf[1] + buf[2]) / 10)
    
def read_infrared():
    i2c.write(0x10, bytearray([0x2B]))
    buf = i2c.read(0x10, 4)   #Auslesen des Signals
    data = buf[3] | (buf[2] << 8) | (buf[1] << 16) | (buf[0] << 24)
    sleep(50)
    return data % 1000  # Reduziert die Zahl auf maximal drei Stellen

    


# FIN
