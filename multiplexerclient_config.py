class multiplexer_config(object):
    '''
    multiplexer client configuration file
    
    Attributes
    ----------
    info: dict
    {channel_name: (port, hint, display_location, stretched, display_pid, dac, dac_rails)}
    '''
    info = {
            '935': (4, '320.571975', (0,3), True, True, 7, [-10.,10.]),
            '638': (8, '469.445150', (0,4), True, True, 3, [-.5,.5])
            }
    ip = '10.97.112.2'
    
