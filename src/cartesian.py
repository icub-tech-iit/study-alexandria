from dataclasses import dataclass, is_dataclass, fields
from phase import Phase
from action import Action
from device import Device
from utils import parse_sysml

class Cartesian(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)
        self.startup = Action
        self.shutdown = Phase
    
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

    def from_sysml(cls, root_path):
        return super().from_sysml(root_path)

    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        extra_attrs = [self.startup, self.shutdown]
        for attr in extra_attrs:
            root.append(super()._extra_attributes(attr))

        self.generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()