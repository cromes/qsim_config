from dataclasses import dataclass
from typing import Tuple

import numpy as np


class ChannelConfiguration:
    """
    Stores complete information for each DAC channel
    'dac_channel_number' is the number of the DAC as defined on the board (as in, what socket it's plugged into)
    'name' is the name of the DAC as will be displayed in the GUI
    'allowed_voltage_range' is the allowable range of the DAC channel, expressed as a tuple
    'displayed' toggles whether the channel is displayed in the GUI
    """
    def __init__(self, dac_channel_number: int,
                 name: str = None,
                 allowed_voltage_range: Tuple[float, float] = (-10, 10),
                 displayed: bool = True):

        self.dac_channel_number: int = dac_channel_number
        self.allowed_voltage_range = allowed_voltage_range
        self.port_name = str(self.dac_channel_number).zfill(2)
        if name:
            self.name = name
        else:
            self.name = "DAC " + self.port_name
        self.displayed = displayed


@dataclass
class Multipole:
    """
    Stores the information on a multipole. i.e. a control that will adjust the DACs in a certain way
    'name' is the name of the multipole, as will be displayed in the GUI
    'effect' is a list of effects of that multipole on the DACs
        That is, the ith element of effect is the multipole's effect on the ith DAC
    'displayed' is a flag that toggles whether the multipole is displayed in the gui
    """
    name: str
    effect: list = None
    displayed: bool = True


class HardwareConfiguration:
    experiment_name = 'Qsim'
    ok_device_id = 'DAC_AD660'
    ok_device_file = 'dac.bit'
    prec_bits = 16
    pulse_triggered = True
    max_cache = 126
    filter_rc = 5e4 * 4e-7
    board_voltage_range = (-10.0, 10.0)

    dac_channels = [
        ChannelConfiguration(4, displayed=False),
        ChannelConfiguration(6, displayed=False),
        ChannelConfiguration(8,  name="End Cap 1", allowed_voltage_range=(0, 10)),
        ChannelConfiguration(10, name="End Cap 2", allowed_voltage_range=(0, 10)),
        ChannelConfiguration(2,  name="RF Rod 1"),
        ChannelConfiguration(17, name="DC Rod 1"),
        ChannelConfiguration(19, name="DC Rod 2"),
        ChannelConfiguration(21, name="RF Rod 2"),
    ]

    @classmethod
    def dac_by_port(cls, port):
        """Convenience method for returning the channel with a specific DAC port"""
        return {chan.dac_channel_number: chan for chan in cls.dac_channels}[port]

    @classmethod
    def dac_by_name(cls, name):
        """Convenience method for returning the channel with a specific name"""
        return {chan.name: chan for chan in cls.dac_channels}[name]


class MultipoleConfiguration:

    multipoles = [
        Multipole("", displayed=False),
        Multipole("", displayed=False),
        Multipole("EC Voltage",    effect=[0, 0, 1,  1, 0, 0,  0,  0]),
        Multipole("EC Difference", effect=[0, 0, 1, -1, 0, 0,  0,  0]),
        Multipole("RF Push",       effect=[0, 0, 0,  0, 1, 0,  0, -1]),
        Multipole("DC Push",       effect=[0, 0, 0,  0, 0, 1, -1,  0]),
        Multipole("DC Squeeze",    effect=[0, 0, 0,  0, 0, 1,  1,  0]),
        Multipole("RF Squeeze",    effect=[0, 0, 0,  0, 1, 0,  0,  1]),
    ]

    # construct the multipole matrix. By default, the multipoles correspond one-to-one with the DAC channels
    M = np.identity(len(multipoles))
    for i, multipole in enumerate(multipoles):
        if multipole.effect:
            M[i] = multipole.effect
    M = M.transpose()
