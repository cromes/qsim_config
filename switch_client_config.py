class switch_config(object):
    '''
    configuration file for multiplexer client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted)), }
    '''
    info = {
            '399 trap': (10, (1, 0), False),
            # 'State Detection Shutter': (12, (3, 0), False),
            'Bad WM Switch': (7, (5, 0), False)
    }

