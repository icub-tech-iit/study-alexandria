from lxml import etree
from dataclasses import dataclass, field, is_dataclass
from device import Device
from utils import parse_sysml, check_subfolders_existance

@dataclass
class Dragonfly(Device):
    width: int
    height: int
    video_type: int
    white_balance: list[float]
    framerate: int
    gain: float
    shutter: float
    brightness: float
    DR2: bool
    stamp: bool
    sharpness: float
    hue: float
    gamma: float
    saturation: float
    guid: str

    def __init__(self, root_path, **kwargs):
        self.folder_name = str
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.__dict__.update(kwargs)

    @classmethod
    def from_sysml(cls, root_path):
        attr = dict(reversed(parse_sysml(root_path + '/templates/dragonfly.sysml').part_definitions.items()))

        for key, value in attr.items():
            for param in value.parameters:
                params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                    for param, val in value.parameters.items()}
        return cls(root_path, **params)

    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self._generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()