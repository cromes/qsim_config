class MultiplexerConfig:
    """
    multiplexer client configuration file

    Attributes
    ----------
    channels: dict
    {channel_name: (port, hint, display_location, stretched, display_pid, dac, dac_rails)}
    """

    channels = {
        "935 [Sebastian]": (4, "320.569062", (0, 3), True, True, 7, [0.0, 10.0]),
        "760 [Stanford]": (5, "394.424944", (0, 4), True, True, 5, [-0.4, 0.4]),
        "Hudson M2": (1, "348.188", (0, 5), True, True, 1, [-10.0, 10.0]),
        "760 [Peter]": (8, "394.424944", (4, 4), True, True, 6, [-1.0, 1.0]),
        # '822':              (1, '364.737',      (0, 5), True, True, 1, [-10.0, 10.0]),
        "935 [Monarch]": (7, "320.571792", (4, 3), True, True, 4, [-10.0, 10.0]),
        # '1108':             (6, '270.430',      (0, 5), True, True, 2, [0.0, 10.0]),
        "935 [downstairs]": (2, "320.571990", (4, 5), True, True, 3, [-10.0, 10.0]),
    }
    ip = "10.97.112.2"
