from microbit import *
import neopixel

np=neopixel.NeoPixel(pin15,3)
np[0] = (20,0,0)
np[1] = (0,0,0)
np[2] = (0,0,0)
np.show()