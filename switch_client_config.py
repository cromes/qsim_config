class switch_config(object):
    """
    configuration file for arduinoTTL client
    info is the configuration dictionary in the form
    {channel_name: (port, inverted)), }
    """
    info = {
            '399 Shutter': (10, True),
            # 'State Detection Shutter': (12, (3, 0), False),
            # 'Bad WM Switch': (7, (5, 0), False)
    }

