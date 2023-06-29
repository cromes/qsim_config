class channelConfiguration(object):
    """
    Stores complete configuration for each of the channels
    """
    def __init__(self, channelNumber, ismanual, manualstate,  manualinversion, autoinversion):
        self.channelnumber = channelNumber
        self.ismanual = ismanual
        self.manualstate = manualstate
        self.manualinv = manualinversion
        self.autoinv = autoinversion


class ddsConfiguration(object):
    """
    Stores complete configuration of each DDS board
    """
    def __init__(self, address, allowedfreqrange, allowedamplrange, frequency, amplitude, **args):
        self.channelnumber = address
        self.allowedfreqrange = allowedfreqrange
        self.allowedamplrange = allowedamplrange
        self.frequency = frequency
        self.amplitude = amplitude
        self.state = True
        self.boardfreqrange = args.get('boardfreqrange', (0.0, 2000.0))
        self.boardramprange = args.get('boardramprange', (0.000113687, 7.4505806))
        self.board_amp_ramp_range = args.get('board_amp_ramp_range', (0.00174623, 22.8896))
        self.boardamplrange = args.get('boardamplrange', (-46.0, 7.0))
        self.boardphaserange = args.get('boardphaserange', (0.0, 360.0))
        self.off_parameters = args.get('off_parameters', (0.0, -46.0))
        self.phase_coherent_model = args.get('phase_coherent_model', True)
        self.remote = args.get('remote', False)
        self.name = None  # will get assigned automatically


class remoteChannel(object):
    def __init__(self, ip, server, **args):
        self.ip = ip
        self.server = server
        self.reset = args.get('reset', 'reset_dds')
        self.program = args.get('program', 'program_dds')


class hardwareConfiguration(object):
    channelTotal = 32
    timeResolution = '40.0e-9'  # seconds
    timeResolvedResolution = 10.0e-9
    maxSwitches = 1022
    resetstepDuration = 3  # duration of advanceDDS and resetDDS TTL pulses in units of time steps
    collectionTimeRange = (0.010, 5.0)  # range for normal pmt counting
    sequenceTimeRange = (0.0, 85.0)  # range for duration of pulse sequence
    isProgrammed = False
    sequenceType = None  # none for not programmed, can be 'one' or 'infinite'
    collectionMode = 'Normal'  # default PMT mode
    collectionTime = {'Normal': 0.100, 'Differential': 0.100}  # default counting rates
    okDeviceID = 'Pulser2'
    okDeviceFile = 'photon_2015_7_13.bit'
    lineTriggerLimits = (0, 15000)  # values in microseconds
    secondPMT = False
    DAC = False

    # name: (channelNumber, ismanual, manualstate,  manualinversion, autoinversion)
    channelDict = {
        # Internal866 is in pulser firmware, this is the required channel name.
        'Internal866':         channelConfiguration(0,  False, False, False, False),  # camera
        '866DP':               channelConfiguration(1,  False, False, True,  False),  # reserved, DiffMode triggering
        '760TTL':              channelConfiguration(2,  False, False, True,  False),
        'WindfreakSynthHDTTL': channelConfiguration(3,  False, False, False, True),
        'MicrowaveTTL':        channelConfiguration(4,  False, False, True,  True),
        'MetastableQubitTTL':  channelConfiguration(5,  False, False, False, False),
        'MicrowaveTTL2':       channelConfiguration(6,  False, False, False, False),
        'TimeHarpMarker':      channelConfiguration(7,  False, False, False, False),
        '411TTL':              channelConfiguration(8,  True,  False, False, False),
        '861SP':               channelConfiguration(9,  False, False, False, False),
        'CameraTrigger':       channelConfiguration(10, False, False, False, False),
        'WindfreakSynthNVTTL': channelConfiguration(11, False, False, True,  True),
        'TTL12':               channelConfiguration(12, False, False, False, True),
        'TTL13':               channelConfiguration(13, False, False, False, False),
        'TTL14':               channelConfiguration(14, False, False, False, False),
        'TTL15':               channelConfiguration(15, False, False, False, False),
        'DiffCountTrigger':    channelConfiguration(16, False, False, False, False),  # reserved
        'TimeResolvedCount':   channelConfiguration(17, False, False, False, False),  # reserved
        'AdvanceDDS':          channelConfiguration(18, False, False, False, False),  # reserved
        'ResetDDS':            channelConfiguration(19, False, False, False, False),  # reserved
        'ReadoutCount':        channelConfiguration(20, False, False, False, False),  # reserved, triggering for analog board
        'TTL21':               channelConfiguration(21, False, False, False, False),
        'TTL23':               channelConfiguration(23, True,  True,  False, False),
        'TTL24':               channelConfiguration(24, False, False, False, False),  # for plotting the clock purpose only
        'TTL25':               channelConfiguration(25, False, False, False, False),
        'TTL26':               channelConfiguration(26, False, True,  False, False),
        'TTL27':               channelConfiguration(27, False, False, False, False),
        'TTL28':               channelConfiguration(28, False, False, False, False),
        'TTL29':               channelConfiguration(29, False, False, False, False),
        'TTL30':               channelConfiguration(30, False, False, False, False),
        'TTL31':               channelConfiguration(31, False, True,  False, False),
                }
    # address, allowedfreqrange, allowedamplrange, frequency, amplitude, **args):
    ddsDict = {
        'OpticalPumpingSP': ddsConfiguration(0,  (80.0, 150.0),  (-46.0, -0.2),  120.0,   -46.0),
        '369DP':            ddsConfiguration(1,  (100.0, 300.0), (-46.0, -4.0),  200.0,   -10.0),
        'StateDetectionSP': ddsConfiguration(2,  (80.0, 150.0),  (-46.0, -4.0),  110.0,   -46.0),
        'RF_Drive':         ddsConfiguration(3,  (30.0, 70.0),   (-46.0, -14.0), 47.835,  -17.1),
        '935SP':            ddsConfiguration(4,  (280.0, 360.0), (-46.0, -8.0),  320.0,   -8.0),
        'DopplerCoolingSP': ddsConfiguration(5,  (80.0, 240.0),  (-46.0, -6.0),  110.0,   -46.0),
        '760SP2':           ddsConfiguration(6,  (120.0, 330.0), (-46.0, 5.0),   160.0,    2.0),
        'Microwave_qubit':  ddsConfiguration(7,  (10.0, 600.0),  (-46.0, 7.0),   467.187, -46.0),
        '760SP':            ddsConfiguration(8,  (90.0, 330.0),  (-46.0, -8.0),  160.0,   -11.0),
        '411DP1':           ddsConfiguration(9,  (400.0, 500.0), (-46.0, -7.2),  450.0,   -46.0),
        '532SP':            ddsConfiguration(10, (65.0,  95.0),  (-46.0, -5.0),  80.0,    -46.0),
        '3GHz_qubit':       ddsConfiguration(11, (100.0, 700.0), (-46.0, -2.0),  250.0,   -46.0),
        '976SP':            ddsConfiguration(12, (250.0, 400.0), (-46.0, 2.0),   320.0,   -46.0),
        # 'ProtectionBeam': ddsConfiguration(11, (100.0, 500.0), (-46.0, -1.0), 250.0, -11.0),
    }
    remoteChannels = {
                    }
