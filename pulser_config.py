from dataclasses import dataclass
from typing import Tuple


@dataclass
class TTLChannel:
    """
    Stores complete configuration of each TTL channel
    """
    channel_number: int
    is_manual: bool
    manual_state: bool
    inverted_manual: bool
    inverted_auto: bool


@dataclass
class DDSChannel:
    """
    Stores complete configuration of each DDS channel
    """
    channel_number: int
    allowed_freq_range: Tuple[float, float]  # MHz/ms
    allowed_ampl_range: Tuple[float, float]  # dB/ms
    frequency: float
    amplitude: float

    state: bool = True
    name: str = None  # will get assigned automatically

    # attributes relating to the phyiscal hardware parameters. Generally shouldn't be touched
    board_freq_range: Tuple[float, float] = (0.0, 2000.0)
    board_ramp_range: Tuple[float, float] = (0.000113687, 7.4505806)  # MHz/ms
    board_amp_ramp_range: Tuple[float, float] = (0.00174623, 22.8896)  # dB/ms
    board_ampl_range: Tuple[float, float] = (-46.0, 7.0)
    board_phase_range: Tuple[float, float] = (0.0, 360.0)
    off_parameters: Tuple[float, float] = (0.0, -46.0)
    phase_coherent_model: bool = True
    is_remote: bool = False


@dataclass
class RemoteDDSChannel:
    """TODO: what does this actually do?"""
    ip: str
    server: str
    reset: str = 'reset_dds'
    program: str = 'program_dds'


class PulserConfiguration:
    """
    Stores the hardware configuration of the Pulser, as well as dicts defining the TTL and DDS channels
    """
    ttl_channel_total = 32
    dds_channel_total = 16

    # settings related to the Pulser hardware
    time_resolution: str = '40.0e-9'  # seconds. this needs to be a string because it gets cast in various ways later
    time_resolved_resolution: float = 10.0e-9  # the resolution of the time tagging in seconds
    max_switches = 1022  # max number of switches that can be in a pulse sequence
    reset_step_duration = 3  # duration of advanceDDS and resetDDS TTL pulses in units of time steps
    collection_time_range = (0.010, 5.0)  # range for normal pmt counting in seconds
    sequence_time_range = (0.0, 85.0)  # range for duration of pulse sequence in seconds
    line_trigger_limits: tuple = (0, 15000)  # values in microseconds
    has_second_pmt: bool = False
    has_dac: bool = False
    ok_device_id: str = 'Pulser2'
    ok_device_file: str = 'photon_2015_7_13.bit'

    # normalPMTflow defaults
    default_collection_mode: str = 'Normal'  # default PMT mode
    default_collection_time: dict = {'Normal': 0.100, 'Differential': 0.100}  # default counting rates

    # name: (channel number, is_manual, manual_state,  manual_inversion, auto_inversion)
    ttl_channel_dict = {
        # Internal866 is in pulser firmware, this is the required channel name.
        'Internal866':         TTLChannel(0,  False, False, False, False),  # camera
        '866DP':               TTLChannel(1,  False, False, True,  False),  # reserved, DiffMode triggering
        '760TTL':              TTLChannel(2,  False, False, True,  False),
        'WindfreakSynthHDTTL': TTLChannel(3,  False, False, False, True),
        'MicrowaveTTL':        TTLChannel(4,  False, False, True,  True),
        'MetastableQubitTTL':  TTLChannel(5,  False, False, False, False),
        'MicrowaveTTL2':       TTLChannel(6,  False, False, False, False),
        'TimeHarpMarker':      TTLChannel(7,  False, False, False, False),
        '411TTL':              TTLChannel(8,  True,  False, False, False),
        '861SP':               TTLChannel(9,  False, False, False, False),
        'CameraTrigger':       TTLChannel(10, False, False, False, False),
        'WindfreakSynthNVTTL': TTLChannel(11, False, False, True,  True),
        'TTL12':               TTLChannel(12, False, False, False, True),
        'TTL13':               TTLChannel(13, False, False, False, False),
        'TTL14':               TTLChannel(14, False, False, False, False),
        'TTL15':               TTLChannel(15, False, False, False, False),
        'DiffCountTrigger':    TTLChannel(16, False, False, False, False),  # reserved
        'TimeResolvedCount':   TTLChannel(17, False, False, False, False),  # reserved
        'AdvanceDDS':          TTLChannel(18, False, False, False, False),  # reserved
        'ResetDDS':            TTLChannel(19, False, False, False, False),  # reserved
        'ReadoutCount':        TTLChannel(20, False, False, False, False),  # reserved, triggering for analog board
        'TTL21':               TTLChannel(21, False, False, False, False),
        'TTL23':               TTLChannel(23, True,  True,  False, False),
        'TTL24':               TTLChannel(24, False, False, False, False),  # for plotting the clock purpose only
        'TTL25':               TTLChannel(25, False, False, False, False),
        'TTL26':               TTLChannel(26, False, True,  False, False),
        'TTL27':               TTLChannel(27, False, False, False, False),
        'TTL28':               TTLChannel(28, False, False, False, False),
        'TTL29':               TTLChannel(29, False, False, False, False),
        'TTL30':               TTLChannel(30, False, False, False, False),
        'TTL31':               TTLChannel(31, False, True,  False, False),
                }
    # address, allowed frequency range, allowed amplitude range, frequency, amplitude, **kwargs):
    dds_channel_dict = {
        'OpticalPumpingSP': DDSChannel(0, (80.0, 150.0), (-46.0, -0.2), 120.0, -46.0),
        '369DP':            DDSChannel(1, (100.0, 300.0), (-46.0, -4.0), 200.0, -10.0),
        'StateDetectionSP': DDSChannel(2, (80.0, 150.0), (-46.0, -4.0), 110.0, -46.0),
        'RF_Drive':         DDSChannel(3, (20.0, 70.0), (-46.0, -5.0), 33.419, -16.0),
        '935SP':            DDSChannel(4, (280.0, 360.0), (-46.0, -8.0), 320.0, -8.0),
        'DopplerCoolingSP': DDSChannel(5, (80.0, 240.0), (-46.0, -6.0), 110.0, -46.0),
        '760SP2':           DDSChannel(6, (120.0, 330.0), (-46.0, 5.0), 160.0, 2.0),
        'Microwave_qubit':  DDSChannel(7, (10.0, 600.0), (-46.0, 7.0), 467.187, -46.0),
        '760SP':            DDSChannel(8, (90.0, 330.0), (-46.0, -8.0), 160.0, -11.0),
        '411DP1':           DDSChannel(9, (400.0, 500.0), (-46.0, -7.2), 450.0, -46.0),
        '532SP':            DDSChannel(10, (65.0, 95.0), (-46.0, -5.0), 80.0, -46.0),
        '3GHz_qubit':       DDSChannel(11, (100.0, 700.0), (-46.0, -2.0), 250.0, -46.0),
        '976SP':            DDSChannel(12, (250.0, 400.0), (-46.0, -4.0), 320.0, -46.0),
        # 'ProtectionBeam': DDSChannelState(11, (100.0, 500.0), (-46.0, -1.0), 250.0, -11.0),
    }
    remote_channels = {}
