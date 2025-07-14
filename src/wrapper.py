from dataclasses import dataclass, fields, is_dataclass
from device import Device
from phase import Phase
from action import Action
from utils import parse_sysml

class Wrapper(Device):
    def __init__(self, root_path, **kwargs):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)

        self.period = float
        self.name = str
        self.startup = Action
        self.shutdown = Phase

    @classmethod
    def from_sysml(cls, root_path):
        attr = parse_sysml(root_path+'/templates/wrapper.sysml').part_definitions
        wrapper = cls(root_path)

        for key, value in attr.items():
            if hasattr(cls, key):
                subclass = getattr(cls, key)
                if is_dataclass(subclass):
                    params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                              for param, val in value.parameters.items()}
                    setattr(wrapper, key, subclass(**params))
            elif key == 'wrapper':
                wrapper.folder_name = value.parameters['folder_name'].strip('"')
            elif key == 'startup':
                wrapper.startup = Action.from_sysml(root_path)
            elif key == 'shutdown':
                wrapper.shutdown = Phase.from_sysml(root_path)
        return wrapper

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