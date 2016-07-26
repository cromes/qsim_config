class arduino_dac_config(object):
    '''
    configuration file for arduino switch client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted)), }
    '''
    info = {'DAC 1': ('Pin 1', 1),
            'DAC 2': ('Pin 2', 2),
	    'DAC 3': ('Pin 4', 3),
	    'DAC 4': ('Pin 5', 4),
	    'DAC 5': ('Pin 6', 5),
            'DAC 6': ('Pin 7', 6),
	    'DAC 7': ('Pin 11', 7),
	    'DAC 8': ('Pin 12', 8),
            }
