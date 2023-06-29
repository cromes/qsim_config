class multiplexer_config(object):
    """
    multiplexer client configuration file

    Attributes
    ----------
    info: dict
    {channel_name: (port, hint, display_location, stretched, display_pid, dac, dac_rails)}
    """
    info = {
        '935 [with EOM]': (4, '320.571975', (0, 3), True, True, 7, [0.0, 10.0]),
        '760 [with EOM]': (5, '394.424944', (0, 4), True, True, 5, [-.4, 0.4]),
        'HudsonM2': (1, '348.188', (0, 5), True, True, 1, [-10.0, 10.0]),
        '760 (Repump)': (8, '444.424944', (4, 4), True, True, 6, [-1.0, 1.0]),
        #'822': (1, '364.737', (0, 5), True, True, 1, [-10.0, 10.0]),
        '976 [currently 935]': (7, '307.058', (4, 5), True, True, 4, [-10.0, 10.0]),
        # '1108': (6, '270.430', (0, 5), True, True, 2, [0.0, 10.0]),
        'ch2': (2, '307.058', (0, 6), True, True, 3, [-10.0, 10.0]),

    }
    ip = '10.97.112.2'
