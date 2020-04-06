class piezo_config(object):
    '''
    Configuration file for piezo controller client.
    Info is the configuration dictionary in the form:
    {channel_name: (port, display_location, inverted)), }
    '''
    info = {'369 Cavity': (1, (1,0), False),
            'Channel 2': (2, (1,1), False),
	    '760': (3, (3,0), False),
	    '760 Repump': (4, (3,1), False)
            }
