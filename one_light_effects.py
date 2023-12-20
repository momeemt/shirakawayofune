import board
import neopixel
import digitalio
import random
import time

LED_PINS = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP16, board.GP17, board.GP26, board.GP27, board.GP28]
LEDS = []

for pin in LED_PINS:
    digout = digitalio.DigitalInOut(pin)
    digout.direction = digitalio.Direction.OUTPUT
    LEDS.append(digout)

pixel_pin = board.GP18
num_pixels = 2
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.6, auto_write=False)

def toggle_leds():
    if random.random() > 0.5:
        LEDS.reverse()
    if random.random() < 0.02:
        fadein_sec = random.randint(5, 15) / 100
        fadeout_sec = random.randint(5, 15) / 100
        for led in LEDS:
            led.value = True
            update_pixels()
            time.sleep(fadein_sec)
            
        for led in LEDS:
            led.value = False
            update_pixels()
            time.sleep(fadeout_sec)

def update_pixels():
    pixels[0] = (0, random.randint(0, 25), random.randint(0, 255))
    pixels[1] = (0, random.randint(0, 25), random.randint(0, 255))
    pixels.show()

while True:
    toggle_leds()
    update_pixels()
    time.sleep(0.1)
