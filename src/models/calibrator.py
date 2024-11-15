from dataclasses import dataclass
from phase import Phase
from device import Device

class Calibrator(Device):
    def __init__(self, level, type, target):
        super().__init__() 
        self.CALIB_ORDER = list[float]
        self.phase = list[Phase(level, type, target)]
    
    @dataclass
    class GENERAL:
        joints: int
        deviceName: str
    @dataclass
    class HOME:
        positionHome = list[float]
        velocityHome = list[float]

    @dataclass
    class CALIBRATION:
        calibrationType = list[float]
        calibration1 = list[float]
        calibration2 = list[float]
        calibration3 = list[float]
        calibration4 = list[float]
        calibration5 = list[float]
        calibrationZero = list[float]
        calibrationDelta = list[float]