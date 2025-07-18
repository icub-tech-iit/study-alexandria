from dataclasses import fields
from device import Device
from phase import Phase
from action import Action

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