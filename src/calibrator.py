from dataclasses import dataclass, is_dataclass, fields
from phase import Phase
from device import Device
from utils import parse_sysml

class Calibrator(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)

        self.CALIB_ORDER = []
        self.startup = Phase
        self.interrupt1 = Phase
        self.interrupt3 = Phase
    
    @dataclass
    class GENERAL:
        joints: int
        deviceName: str
    @dataclass
    class HOME:
        positionHome: list[float]
        velocityHome: list[float]
    @dataclass
    class CALIBRATION:
        calibrationType: list[float]
        calibration1: list[float]
        calibration2: list[float]
        calibration3: list[float]
        calibration4: list[float]
        calibration5: list[float]
        calibrationZero: list[float]
        calibrationDelta: list[float]
        startupPosition: list[int]
        startupVelocity: list[int]
        startupMaxPwm: list[int]
        startupPosThreshold: list[int]

    @classmethod
    def from_sysml(cls, root_path):
        return super().from_sysml(root_path)
    
    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)
        extra_attrs = [self.startup, self.interrupt1, self.interrupt3]
        for attr in extra_attrs:
            root.append(super()._extra_attributes(attr))

        self.generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()