class channelConfiguration(object):
    """
    Stores complete information for each DAC channel
    """

    def __init__(self, dacChannelNumber, trapElectrodeNumber = None,
                 octantNumber = None, name = None, boardVoltageRange = (-10, 10),
                 allowedVoltageRange = (-10, 10)):
        
        self.dacChannelNumber = dacChannelNumber
        self.trapElectrodeNumber = trapElectrodeNumber
        self.octantNumber = octantNumber
        self.boardVoltageRange = boardVoltageRange
        self.allowedVoltageRange = allowedVoltageRange
        if (name == None) & (trapElectrodeNumber != None):
            self.name = str(trapElectrodeNumber).zfill(2)
        else:
            self.name = name

    def computeDigitalVoltage(self, analogVoltage):
        return int(round(sum([ self.calibration[n] * analogVoltage ** n for n in range(len(self.calibration)) ])))


class hardwareConfiguration(object):
    EXPNAME = 'Qsim'
    okDeviceID = 'DAC_AD660'
    okDeviceFile = 'dac.bit'
    PREC_BITS = 16
    pulseTriggered = True
    maxCache = 126
    filter_RC = 5e4 * 4e-7

    elec_dict = {
        '0': channelConfiguration(2, trapElectrodeNumber=2),
        '1': channelConfiguration(4, trapElectrodeNumber=4),
        '2': channelConfiguration(6, trapElectrodeNumber=6),
        '3': channelConfiguration(8, trapElectrodeNumber=8),
        '4': channelConfiguration(10, trapElectrodeNumber=10),
        '5': channelConfiguration(15, trapElectrodeNumber=15),
        '6': channelConfiguration(17, trapElectrodeNumber=17),
        '7': channelConfiguration(19, trapElectrodeNumber=19),
        #'8': channelConfiguration(21, trapElectrodeNumber=21)
        }
