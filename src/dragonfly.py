from dataclasses import dataclass, fields, is_dataclass
from device import Device
from utils import parse_sysml

class Dragonfly(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)

        self.width = int
        self.height = int
        self.video_type = int 
        self.white_balance = list[float]
        self.framerate = int
        self.gain = float
        self.shutter = float
        self.brightness = float
        self.DR2 = bool
        self.stamp = bool
        self.sharpness = float
        self.hue = float
        self.gamma = float
        self.saturation = float
        self.guid = str

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