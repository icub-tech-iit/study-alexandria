from dataclasses import dataclass, fields
from device import Device

class Realsense(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)

    @dataclass
    class SETTINGS:
        depthResolution: list[int]
        rgbResolution: list[int]
        framerate: int
        enableEmitter: bool
        needAlignment: bool
        alignmentFrame: str
    @dataclass
    class HW_DESCRIPTION:
        clipPlanes: list[float]

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