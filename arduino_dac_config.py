class arduino_dac_config(object):
    '''
    configuration file for arduino switch client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted)), }
    '''
    info = {'DAC 1': ('Pins 5 and 6', 1),
            'DAC 2': ('Pins 2 and 11', 2),
	    'DAC 3': ('Pins 4 and 7', 3),
	    'DAC 4': ('NC', 4),
	    'DAC 5': ('Pins 1 and 12', 5),
            'DAC 6': ('NC', 6),
	    'DAC 7': ('NC', 7),
	    'DAC 8': ('NC', 8),
            }
