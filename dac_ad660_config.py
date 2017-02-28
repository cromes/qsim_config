class channelConfiguration(object):
    """
    Stores complete information for each DAC channel
    """

    def __init__(self, dacChannelNumber, trapElectrodeNumber = None,
                 octant = None, name = None, boardVoltageRange = (-10, 10),
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
