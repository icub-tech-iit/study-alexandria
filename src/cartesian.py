from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from phase import Phase
from action import Action
from device import Device
from utils import parse_sysml, check_subfolders_existance

class Cartesian(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.startup = Action
        self.shutdown = Phase
        self.folder_name = str
    
    @dataclass
    class GENERAL:
        ControllerName: str
        ControllerPeriod: int
        TaskRefVelPeriodFactor: int
        SolverNameToConnect: str
        KinematicPart: str
        KinematicType: str
        PositionControl: str
        NumberOfDrivers: int
    @dataclass
    class DRIVER_0:
        Key: str
        JointsOrder: str
        MinAbsVels: list[float]
    @dataclass
    class DRIVER_1:
        Key: str
        JointsOrder: str
        MinAbsVels: list[float]
    @dataclass
    class PLANT_MODEL:
        plant_compensator: str
        smith_predictor: str
        joint_0: list[str]
        joint_1: list[str]
        joint_2: list[str]
        joint_3: list[str]
        joint_4: list[str]
        joint_5: list[str]
        joint_6: list[str]
        joint_7: list[str]
        joint_8: list[str]
        joint_9: list[str]

    @classmethod
    def from_sysml(cls, root_path):
        attr = parse_sysml(root_path+'/templates/cartesian.sysml').part_definitions
        cartesian = cls(root_path)

        for key, value in attr.items():
            if hasattr(cls, key):
                subclass = getattr(cls, key)
                if is_dataclass(subclass):
                    params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                    setattr(cartesian, key, subclass(**params))
            elif key in ['shutdown']:
                setattr(cartesian, key, Phase.from_sysml(root_path))
            elif key in ['startup']:
                setattr(cartesian, key, Action.from_sysml(root_path))
            elif key == 'cartesian':
                cartesian.folder_name = value.parameters['folder_name'].strip('"')
        return cartesian

    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        extra_attrs = [self.startup, self.shutdown]
        for attr in extra_attrs:
            root.append(super()._extra_attributes(attr))

        self._generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()