#Micropython, Calliopemini3, Calllibot2
# Steuerung über I2C-Adr 0x22 und Register

from microbit import *
import utime

i2c.init()
#i2c.write(0x22,[0x01])    #reset

led_puffer = bytearray(5)
led_puffer[0] = 0x03   # leds 
led_puffer[1] = 0x06   # r led (gruen)
led_puffer[2] = 0x08  # 1-16?
i2c.write(0x22, led_puffer)
utime.sleep_ms(1000)
led_puffer[1] = 0x05   # linke led (rot)
i2c.write(0x22, led_puffer)
utime.sleep_ms(1000)

reset_puffer = bytearray(1)
reset_puffer[0] = 0x01
i2c.write(0x22, reset_puffer)


