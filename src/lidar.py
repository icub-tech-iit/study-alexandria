from dataclasses import dataclass, fields
from device import Device

class Lidar(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)

    @dataclass
    class GENERAL:
        name: str
        serial_baudrate: int
        serial_port: str
        sample_buffer_life: int
    @dataclass
    class SENSOR:
        max_distance: float
        min_distance: float
        max_angle: int
        min_angle: int
        resolution: float
        allow_infinity: int
    @dataclass
    class RPLIDAR:
        scan_mode: str

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