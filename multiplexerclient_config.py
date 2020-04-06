class multiplexer_config(object):
    '''
    multiplexer client configuration file
    
    Attributes
    ----------
    info: dict
    {channel_name: (port, hint, display_location, stretched, display_pid, dac, dac_rails)}
    '''
    info = {
            '935': (4, '320.571975', (0, 3), True, True, 7, [0.0, 10.0]),
            '760': (5, '555.424', (0, 4), True, True, 5, [-.4, 0.4]),
            '760 (Repump)': (3, '494.424', (6, 4), True, True, 6, [-10.0, 10.0]),
            '411': (2, '729.474', (6,3), True, True, 3, [-10.0,10.0]),
            #'399': (8, '751.527', (0,5), True, True, 8, [-10.0,10.0]),
            '976': (7,'307.058',(6,5),True,True,4,[-10.0,10.0]),
            }
    ip = '10.97.112.2'
