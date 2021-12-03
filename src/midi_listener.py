import mido


class MidiListener():

    def __init__(self):
        self.callback = None

    def message_is_valid(self, message):
        """Determines if the incoming message is a key press"""
        valid_messages = [
            'note_on',
            'note_off',
        ]
        return message.type in valid_messages

    def set_callback(self, callback_function):
        """Sets a callback function for the particular note"""
        self.callback = callback_function

    def listen(self):
        """Listens for incoming events from MIDI device"""
        print('Starting listening...')
        try:
            keyboard_name = mido.get_input_names()[1]
        except IndexError:
            keyboard_name = None
        with mido.open_input(keyboard_name) as inport:
            for message in inport:
                if self.message_is_valid(message):
                    self.callback(message)


if __name__ == "__main__":
    ml = MidiListener()
    ml.listen()
