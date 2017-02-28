class switch_config(object):
    '''
    configuration file for multiplexer client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted)), }
    '''
    info = {
            '399 trap': (10, (1, 0), True),
	    'CW 369 (ML overlay)': (9, (2, 0), False),
	    'Mode Locked 369': (12, (3, 0), False),
	    'CW 369': (11, (0,0), False)
            }
