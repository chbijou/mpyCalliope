# Micropython Calliopemini3 Callibot2E
# Spurensensoren auslesen
# i2c-adresse 0x22 i2c-Register 0x84

from microbit import *

i2c.init()
sensor_puffer = bytearray(5)
sensor_puffer[0] = 0x84   #Spurensensoren triggern
i2c.write(0x22, sensor_puffer)

sensor_puffer=i2c.read(0x22,5)

rechts_wert = sensor_puffer[1] + 256 * sensor_puffer[2]
links_wert  = sensor_puffer[3] + 256 * sensor_puffer[4]

print("rechts= ",rechts_wert, "links= ",links_wert)
