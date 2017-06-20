import numpy as np

class channelConfiguration(object):
    """
    Stores complete information for each DAC channel
    """

    def __init__(self, dacChannelNumber, octantNumber = None,
                 name = None, boardVoltageRange = (-10, 10),
                 allowedVoltageRange = (-10, 10)):

        self.dacChannelNumber = dacChannelNumber
        self.octantNumber = octantNumber
        self.boardVoltageRange = boardVoltageRange
        self.allowedVoltageRange = allowedVoltageRange
        if (name == None) & (octantNumber != None):
            self.name = str(dacChannelNumber).zfill(2)
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
        '02': channelConfiguration(2, octantNumber=2),
        '04': channelConfiguration(4, octantNumber=3),
        '06': channelConfiguration(6, octantNumber=4),
        '08': channelConfiguration(8, octantNumber=8),
        '10': channelConfiguration(10, octantNumber=7),
        '15': channelConfiguration(15, octantNumber=6),
        '17': channelConfiguration(17, octantNumber=5),
        '19': channelConfiguration(19, octantNumber=1),
        }

    row_1 = [-7.98491456e+04, 9.97290504e+03, -8.34753779e+02,
                 7.83711367e+05, 1.60632984e+06, 2.07110112e+09,
                 -9.21613019e+05, -6.47489511e+06]

    row_4 = [9.08217330e+04, -1.26262665e+04, 1.72276248e+03,
                 -8.77337835e+05, -1.19566908e+06, -2.31777025e+09,
                 8.72739472e+05, 7.40424900e+06]

    row_3 = [-8.33511849e+04, 1.00807327e+04, -8.42031614e+02,
                 7.83322761e+05, 1.61682392e+06, 2.09390837e+09,
                 -9.31852246e+05, -6.83102436e+06]

    row_2 = [7.74809889e+04, -8.14548331e+03, 1.46261072e+03,
                 -7.39129168e+05, -1.03420689e+06, -1.97729719e+09,
                 1.02982636e+06, 6.31653529e+06]

    row_5 = [7.83056368e+04, -9.35883102e+03, 7.44032820e+02,
                 -3.96139461e+03, -1.02615220e+06, -1.96518036e+09,
                 8.83825337e+05, 6.13498121e+06]

    row_8 = [-7.50714648e+04, 7.79852359e+03, -1.41418832e+03,
                 -1.51076112e+04, 1.52982245e+06, 1.91561317e+09,
                 -7.22981923e+05, -6.11870080e+06]

    row_7 = [7.54130105e+04, -9.32179831e+03, 7.41447591e+02,
                 -3.88766024e+03, -1.02233674e+06, -1.95737952e+09,
                 8.80325442e+05, 6.39450469e+06]

    row_6 = [-8.01616368e+04, 1.10981675e+04, -1.51302236e+03,
                 3.74643059e+04, 1.59176500e+06, 2.04552764e+09,
                 -1.05562593e+06, -6.53377462e+06]

    row_1 = [-1., 0., 1., 0., -1., 0., 1., 0.]
    row_2 = [0., 1., 0., -1., 0., 1., 0., -1.]
    row_3 = [-1., -1., -1., -1., 1., 1., 1. ,1.]
    row_4 = [1., 1., 1., 1., 1., 1., 1., 1.]
    row_5 = [1., -1., 1., -1., 1., -1., 1., -1.]
    row_6 = [1., 0., -1., 0., -1., 0., 1., 0.]
    row_7 = [0., -1., 0., 1., 0., 1., 0., -1.]
    row_8 = [1/3., -1.0, 5/3., -1.0, -1/3., 1., -5/3., 1.]

    U = np.array([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8])
    M = np.linalg.inv(U)
