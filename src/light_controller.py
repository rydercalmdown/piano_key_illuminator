import os
import time
import board
import neopixel
import logging


class LightController():
    """Class for controlling LEDs"""

    def __init__(self):
        """Instantiate the module"""
        self._set_defaults()
    
    def setup(self):
        """Initiate setup, once everything is complete"""
        self._setup_neopixels()

    def _set_defaults(self):
        """Setup the defaults"""
        self.highest_key = None
        self.lowest_key = None
        self.led_count = None
        self.pin = board.D18 
        self.brightness = 1

    def _setup_neopixels(self):
        self.pixels = neopixel.NeoPixel(
            self.pin,
            self.led_count,
            brightness=self.brightness,
            auto_write=False,
            pixel_order=neopixel.RGB
        )

    def _convert_key_to_led(self, key):
        """Converts the current key being played to a LED"""
        if key > self.highest_key:
            logging.debug('Key out of bounds - too high')
            return None
        if key < self.lowest_key:
            logging.debug('Key out of bounds - too low')
            return None
        total_avail_keys = self.highest_key - self.lowest_key
        leds_per_key = total_avail_keys / self.led_count
        return int(round(((key - self.lowest_key) * self.led_count) / total_avail_keys))

    def iterate_leds(self, num_times=3, delay=0.01):
        """Iterate over and illuminate the LEDs"""
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
        for _ in range(0, num_times):
            for i in range(0, self.led_count - 1):
                self.pixels[i] = [255, 255, 255]
                if i - 1 >= 0:
                    self.pixels[i - 1] = [0, 0, 0]
                self.pixels.show()
                time.sleep(delay)
            self.pixels.fill((0, 0, 0))
            self.pixels.show()

    def flash_leds(self, num_times=3, delay=0.3):
        """Flashes all the LEDs"""
        logging.info('Flashing LEDs')
        for _ in range(0, num_times):
            self.pixels.fill((255, 255, 255))
            self.pixels.show()
            time.sleep(delay)
            self.pixels.fill((0, 0, 0))
            self.pixels.show()
            time.sleep(delay)

    def test(self):
        """Tests the lights"""
        self.iterate_leds()
        self.flash_leds()

    def illuminate_key(self, key):
        """Turn a particular key on"""
        led = self._convert_key_to_led(key)
        if led is not None:
            self.pixels[led] = (255, 255, 255)
            self.pixels.show()

    def deilluminate_key(self, key):
        """Turn a particular key off"""
        led = self._convert_key_to_led(key)
        if led is not None:
            self.pixels[led] = (0, 0, 0)
            self.pixels.show()

    def turn_leds_on(self):
        """Turns the LEDs on"""
        self.flash_leds()
        logging.info('Turning LEDs On')
        self.pixels.fill((255, 255, 255))
        self.pixels.show()
    
    def turn_leds_off(self):
        """Turns the LEDs off"""
        logging.info('Turning LEDs Off')
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
