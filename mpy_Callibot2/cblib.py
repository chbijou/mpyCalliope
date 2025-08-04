#Micropython Calliope mini3 Callibit2
from microbit import*

#Initialisiere Callibot
i2c.init()

def motorL(dir, speed):
    buf_motor1 = bytearray(3)
    buf_motor1[0] = 0x00  # Motor auswählen - 0x00: Motor rechts
    buf_motor1[1] = dir  # Richtung auswählen 0:vorwärts | 1:rückwärts
    buf_motor1[2] = speed   # Geschwindigkeit von 0 - 255
    i2c.write(0x10, buf_motor1)

def motorR(dir, speed):
    buf_motor2 = bytearray(3)
    buf_motor2[0] = 0x02   #Motor auswählen - 0x02: Motor links
    buf_motor2[1] = dir   #Richtung auswählen 0:vorwärts | 1:rückwärts
    buf_motor2[2] = speed   #Geschwindigkeit von 0 - 255
    i2c.write(0x10, buf_motor2)

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
    
def rgbLed(red, green, blue):
    # Alle 4 RGB-LEDs gleichzeitig schalten
    # Prinzip MotionKit2
    buf_rgbLed = bytearray(5)
    buf_rgbLed[0] = 0x03
    for index in range(4):
        buf_rgbLed[1] = index+1
        buf_rgbLed[2] = red
        buf_rgbLed[3] = green
        buf_rgbLed[4] = blue
        i2c.write(0x22, buf_rgbLed)

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

def black_line():
# 0: ganz ausserhalb
# 1: rechts ausserhalb
# 2: links ausserhalb
# 3_ mitten auf der Spur
    i2c.write(0x10,bytearray([0x1D]))
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
    buf = i2c.read(0x10, 4)   #Auslesen des Signals
    data = buf[3] | (buf[2] << 8) | (buf[1] << 16) | (buf[0] << 24)
    sleep(50)
    return data % 1000  # Reduziert die Zahl auf maximal drei Stellen

    


# FIN
