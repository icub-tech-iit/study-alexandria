from dataclasses import dataclass
from base import BaseClass
class Mechanicals(BaseClass):
    def __init__(self, root_path):
        super().__init__()
    @dataclass
    class GENERAL:
        MotioncontrolVersion: int
        Joints: int
        AxisMap: list[int]
        AxisName: list[str]
        AxisType: list[str]
        Encoder: list[float]
        fullscalePWM: list[int]
        ampsToSensor: list[float]
        Gearbox_M2J: list[float]
        Gearbox_E2J: list[int]
        useMotorSpeedFbk: list[int]
        MotorType: list[str]
        Verbose: int
    @dataclass
    class LIMITS:
        hardwareJntPosMin: list[int]
        hardwareJntPosMax: list[int]
        rotorPosMin: list[int]
        rotorPosMax: list[int]
    @dataclass
    class _2FOC:
        HasHallSensor: list[int]
        HasTempSensor: list[int]
        HasRotorEncoder: list[int]
        HasRotorEncoderIndex: list[int]
        HasSpeedEncoder: list[int]
        RotorIndexOffset: list[int]
        MotorPoles: list[int]         
    @dataclass
    class COUPLINGS:
        matrixJ2M: list[list[float]]
        matrixM2J: list[list[float]]
        matrixE2J: list[list[float]]
    @dataclass
    class JOINTSET_CFG:
        numberofsets: int
        @dataclass
        class JOINTSET_0:
            listofjoints: list[int]
            _constraint: str
            param1: int
            param2: int
        @dataclass
        class JOINTSET_1:
            listofjoints: list[int]
            _constraint: str
            param1: int
            param2: int
        @dataclass
        class JOINTSET_2:
            listofjoints: list[int]
            _constraint: str
            param1: int
            param2: int
        @dataclass
        class JOINTSET_3:
            listofjoints: list[int]
            _constraint: str
            param1: int
            param2: int
        JOINTSET_0: JOINTSET_0
        JOINTSET_1: JOINTSET_1
        JOINTSET_2: JOINTSET_2
        JOINTSET_3: JOINTSET_3

    @classmethod
    def from_sysml(cls, root_path):
        return super().from_sysml(root_path)
    
    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self.generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()