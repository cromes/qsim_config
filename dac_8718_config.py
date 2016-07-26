

class DACChannel(object):
    """
    Channel name and number for a single DAC channel.

    Parameters
    ----------
    name: str, 'DAC 0', etc., default(None)
    number: int, channel number, starting with 0, default(None)
    """
    def __init__(self, name, number):
        self.name = name
        self.number = number


class dac_8718_config(object):
    '''
    configuration file for arduino switch client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted)), }
    '''
    channels = {}
    channels['DAC 1'] = DACChannel(name='DAC 0', number=0)
    channels['DAC 2'] = DACChannel(name='DAC 1', number=1)
    channels['DAC 3'] = DACChannel(name='DAC 2', number=2)
    channels['DAC 4'] = DACChannel(name='DAC 3', number=3)
    channels['DAC 5'] = DACChannel(name='DAC 4', number=4)
    channels['DAC 6'] = DACChannel(name='DAC 5', number=5)
    channels['DAC 7'] = DACChannel(name='DAC 6', number=6)
    channels['DAC 8'] = DACChannel(name='DAC 7', number=7)
