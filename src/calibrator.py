from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from phase import Phase
from device import Device
from utils import parse_sysml, check_subfolders_existance

@dataclass
class Calibrator(Device):
    CALIB_ORDER: list[float]    
    def __init__(self, root_path):
        self.includes = str
        self.folder_name = str
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        # self.CALIB_ORDER = list[float]
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
        attr = parse_sysml(root_path+'/templates/calibrator.sysml').part_definitions
        calib = cls(root_path)

        for key, value in attr.items():
            if hasattr(cls, key):
                subclass = getattr(cls, key)
                if is_dataclass(subclass):
                    params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                    setattr(calib, key, subclass(**params))
            elif key == 'calibrator':
                calib.CALIB_ORDER = [x for x in value.parameters['CALIB_ORDER'].strip('"').split(',')]
                calib.includes = value.parameters['includes'].strip('"')
                calib.folder_name = value.parameters['folder_name'].strip('"')
            elif key in ['startup', 'interrupt1', 'interrupt3']:
                setattr(calib, key, Phase.from_sysml(root_path))
        return calib

    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        extra_attrs = [self.startup, self.interrupt1, self.interrupt3]
        for attr in extra_attrs:
            root.append(super()._extra_attributes(attr))

        self._generate_xml(root, root_path, file_name)

def main():
    # pass
    cal = Calibrator.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    cal.to_xml('/home/mgloria/iit/study-alexandria/sysml', 'calibrator.xml')

if __name__ == "__main__":
    main()