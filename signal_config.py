
import random


class SignalConfig(dict):
    """
    A complete dictionary of all signals with unique IDs and properties of the data content.
    """
    def __init__(self):
        # Define available signals. Keys must have format f'{server}__{signal}'.
        super().__init__(
            normalpmtflow__new_count=(None, 'signal: new count', 'v'),
            normalpmtflow__new_setting=(None, 'signal: new setting', '(ss)')
        )

        # Generate unique IDs
        ids = random.sample(range(100000, 1000000), len(self))
        for i, (k, v) in enumerate(self.items()):
            self[k] = (ids[i], ) + v[1:]

        self.signal = {v[0]: k for k, v in self.items()}

    def get_id(self, signal):
        return self.get(signal, None)[0]

    def get_server(self, signal_or_id):
        if isinstance(signal_or_id, int):
            signal = self.signal[signal_or_id]
        else:
            signal = signal_or_id
        return signal[:signal.find('__')]

    def get_signal(self, signal_or_id):
        if isinstance(signal_or_id, int):
            signal = self.signal[signal_or_id]
        else:
            signal = signal_or_id
        return signal[signal.find('__')+2:]


signal_config = SignalConfig()
