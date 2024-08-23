import numpy as np


class channelConfiguration:
    """
    Stores complete information for each DAC channel
    """

    def __init__(self, dacChannelNumber, octantNumber=None,
                 name=None, boardVoltageRange=(-10, 10),
                 allowedVoltageRange=(-10, 10)):

        self.dacChannelNumber = dacChannelNumber
        self.octantNumber = octantNumber
        self.boardVoltageRange = boardVoltageRange
        self.allowedVoltageRange = allowedVoltageRange
        if (name is None) and (octantNumber is not None):
            self.name = str(dacChannelNumber).zfill(2)
        else:
            self.name = name

    def computeDigitalVoltage(self, analogVoltage):
        return int(round(sum([self.calibration[n] * analogVoltage ** n for n in range(len(self.calibration))])))


class hardwareConfiguration(object):
    EXPNAME = 'Qsim'
    okDeviceID = 'DAC_AD660'
    okDeviceFile = 'dac.bit'
    PREC_BITS = 16
    pulseTriggered = True
    maxCache = 126
    filter_RC = 5e4 * 4e-7

    elec_dict = {
        # '02': channelConfiguration(2, octantNumber=2),
        '04': channelConfiguration(4, octantNumber=3),
        '06': channelConfiguration(6, octantNumber=4),
        '08': channelConfiguration(8, octantNumber=8),
        '10': channelConfiguration(10, octantNumber=7),
        # '15': channelConfiguration(15, octantNumber=6),
        '02': channelConfiguration(2, octantNumber=6),
        '17': channelConfiguration(17, octantNumber=5),
        '19': channelConfiguration(19, octantNumber=1),
        '21': channelConfiguration(21, octantNumber=2),
    }

    row_1 = np.array(
        [-0.13498456133340694, -0.22822763173002142, 0.8961134561077739, 0, 0.03079106488049214, 0.061580416233014384,
         -0.20866367019066936, 0.3146372093425512])
    row_2 = np.array(
        [0.8908677523569054, -0.20232240687699407, 0.10459422303466558, 0, -0.20455528194084024, 0.128366358869311,
         -0.023324998349689808, -0.335157471529991])
    row_3 = np.array(
        [0.12268222110660028, -0.2638522962295497, -0.9274190352785705, 0, -0.02646419382021535, 0.03115752187583479,
         0.20209137924927514, 0.3410298415114044])
    row_4 = np.array(
        [-0.8765554647137599, -0.17922447767291022, -0.12563455663077122, 0, 0.20759828815865433, 0.19285468560318647,
         0.030300397218941455, -0.31385946581509216])
    row_5 = np.array(
        [-0.2100106250890763, 0.22208753702210055, 0.9671694632771416, 0, -0.04382552470478926, 0.0497666601847018,
         0.22580283679050323, 0.3093072300606508])
    row_6 = np.array(
        [0.987831946648141, 0.26438036034329593, 0.11199323226537358, 0, 0.20737301081275314, 0.2046320419197635,
         0.018937520605854043, -0.3227544080980987])
    row_7 = np.array(
        [0.1332747750154683, 0.2069630438004031, -0.9666920243244032, 0, 0.03767675901041993, 0.06522729778134241,
         -0.2082755486957026, 0.3280261759999269])
    row_8 = np.array(
        [-1.0288431186184475, 0.2814295570069129, -0.07830764109604008, 0, -0.2333719967049315, 0.1307833142941775,
         -0.017884128780203, -0.30648565934440636])
    M = np.array([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8])
    # U = np.linalg.inv(M)

#   row_1 = [-1., 0., 1., 0., -1., 0., 1., 0.]
#   row_2 = [0., 1., 0., -1., 0., 1., 0., -1.]
#   row_3 = [-1., -1., -1., -1., 1., 1., 1. ,1.]
#   row_4 = [1., 1., 1., 1., 1., 1., 1., 1.]
#   row_5 = [1., -1., 1., -1., 1., -1., 1., -1.]
#   row_6 = [1., 0., -1., 0., -1., 0., 1., 0.]
#   row_7 = [0., -1., 0., 1., 0., 1., 0., -1.]
#   row_8 = [1/3., -1.0, 5/3., -1.0, -1/3., 1., -5/3., 1.]

#    U = np.array([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8])
#    M = np.linalg.inv(U)
