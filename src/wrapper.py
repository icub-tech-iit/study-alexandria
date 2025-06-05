from lxml import etree
from dataclasses import dataclass
from device import Device
from phase import Phase
from action import Action
from utils import parse_sysml, check_subfolders_existance

@dataclass
class Wrapper(Device):
    period: float
    name: str
    startup: Action
    shutdown: Phase

    def __init__(self, root_path, **kwargs):
        self.folder_name = str
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.__dict__.update(kwargs)

    @classmethod
    def from_sysml(cls, root_path):
        attr = parse_sysml(root_path+'/templates/wrapper.sysml').part_definitions
        params = {}
        for key, value in attr.items():
            for param in value.parameters:
                params.update({param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                    for param, val in value.parameters.items()})
            if key == 'startup':
                params.update({key: Action.from_sysml(root_path)})
            elif key == 'shutdown':
                params.update({key: Phase.from_sysml(root_path)})
        return cls(root_path, **params)

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