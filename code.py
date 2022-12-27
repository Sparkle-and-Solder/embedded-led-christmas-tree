import board
import neopixel

from adafruit_led_animation.sequence import AnimationSequence
# from adafruit_led_animation.animation.customcolorchase import CustomColorChase
#from adafruit_led_animation.animation.blink import Blink
# from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.color import PURPLE, WHITE, AMBER, JADE, MAGENTA, ORANGE

pixel_pin = board.A1
num_pixels = 25

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
colorcycle = ColorCycle(pixels, speed=0.4, colors=[MAGENTA, ORANGE])

#blink = Blink(pixels, speed=0.5, color=JADE)

animations = AnimationSequence(
    colorcycle,
    #blink,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
