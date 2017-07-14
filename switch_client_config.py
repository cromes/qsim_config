class switch_config(object):
    '''
    configuration file for multiplexer client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted)), }
    '''
    info = {
            '399 trap': (10, (1, 0), True),
	    '369/399 Wavemeter': (9, (2, 0), False),
	    'ML to Trap': (12, (3, 0), False),
            }
