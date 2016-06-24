class switch_config(object):
    '''
    configuration file for multiplexer client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted)), }
    '''
    info = {
            '399 trap': (10, (0, 2), True),
            '369 wavemeter': (9, (0, 3), False),
            }
