import minimalmodbus




avail_channels = [ 'V_IN0', 'V_IN1', 'V_IN2', 'V_IN3', 'V_IN4', 'V_IN5', 'V_IN6', 'V_IN7' ]

class DC_V:
    def __init__(self):
        self.__device = minimalmodbus.Instrument('/dev/dkst1101/COM11', 1)

    def init(self):
        pass

    def Get(self, channel):
        pass
