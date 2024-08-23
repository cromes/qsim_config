import numpy as np


class ChannelConfiguration:
    """
    Stores complete information for each DAC channel
    """

    def __init__(self, dac_channel_number,
                 name=None,
                 board_voltage_range=(-10, 10),
                 allowed_voltage_range=(-10, 10)):

        self.dac_channel_number = dac_channel_number
        self.board_voltage_range = board_voltage_range
        self.allowed_voltage_range = allowed_voltage_range
        self.port_name = str(self.dac_channel_number)
        if len(self.port_name) == 1:
            self.port_name = "0" + self.port_name
        if name is None:
            self.name = "DAC " + str(dac_channel_number).zfill(2)
        else:
            self.name = name


class HardwareConfiguration:
    EXPNAME = 'Qsim'
    okDeviceID = 'DAC_AD660'
    okDeviceFile = 'dac.bit'
    PREC_BITS = 16
    pulseTriggered = True
    maxCache = 126
    filter_RC = 5e4 * 4e-7

    dac_channels = [
        ChannelConfiguration(4),
        ChannelConfiguration(6),
        ChannelConfiguration(8,  name="End Cap 1", allowed_voltage_range=(0, 10)),
        ChannelConfiguration(10, name="End Cap 2", allowed_voltage_range=(0, 10)),
        ChannelConfiguration(2,  name="RF Rod 1"),
        ChannelConfiguration(17, name="DC Rod 1"),
        ChannelConfiguration(19, name="DC Rod 2"),
        ChannelConfiguration(21, name="RF Rod 2"),
    ]

    """The columns of M are the calibrations of the multipoles. """

    M = np.array([
        [1,   0,   0,   0,   0,   0,   0,   0],
        [0,   1,   0,   0,   0,   0,   0,   0],
        [0,   0,   1,   1,   0,   0,   0,   0],
        [0,   0,   1,  -1,   0,   0,   0,   0],
        [0,   0,   0,   0,   1,   0,   0,   1],
        [0,   0,   0,   0,   0,   1,   1,   0],
        [0,   0,   0,   0,   0,  -1,   1,   0],
        [0,   0,   0,   0,  -1,   0,   0,   1],
    ])
