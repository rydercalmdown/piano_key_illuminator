import os
import logging

from light_controller import LightController
from midi_listener import MidiListener


class PianoKeyIlluminator():
    """Class for running the piano key illuminator application"""

    def __init__(self):
        """Setup"""
        self.lc = LightController()
        self.ml = MidiListener()
        self._setup_defaults()

    def _setup_defaults(self):
        """Setup default settings"""
        logging.debug('Setting application defaults')
        self.ml.set_callback(self.key_callback)
        self.lc.highest_key = 101
        self.lc.lowest_key = 30
        self.lc.led_count = 60
        self.lc.setup()

    def key_callback(self, message):
        """Callback function for key event"""
        key = int(message.note)
        logging.info(str(key) + ' - ' + str(message.type))
        if message.type == 'note_on':
            self.lc.illuminate_key(key)
        if message.type == 'note_off':
            self.lc.deilluminate_key(key)

    def run(self):
        """Run the application"""
        try:
            logging.info('Starting application')
            logging.info('Testing LEDs')
            self.lc.test()
            logging.info('Starting MIDI listener')
            self.ml.listen()
        except KeyboardInterrupt:
            logging.info('Exiting')


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    pki = PianoKeyIlluminator()
    pki.run()
