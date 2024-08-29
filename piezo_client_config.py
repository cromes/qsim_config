class piezo_config(object):
    """
    Configuration file for piezo controller client.
    Info is the configuration dictionary in the form:
    {channel_name: (port, display_location, inverted)), }
    """
    # 2x2 grid arrangement
    # info = {'1': (1, (1, 0), False),
    #         '2': (2, (1, 1), False),
    #         '3': (3, (3, 0), False),
    #         '4': (4, (3, 1), False),
    #         }

    # 1x4 horizontal line arrangement
    info = {'1': (1, (1, 0), False),
            '2': (2, (1, 1), False),
            '3': (3, (1, 2), False),
            '4': (4, (1, 3), False),
            }

