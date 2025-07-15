from dataclasses import dataclass, fields
from device import Device

class FT(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)
        self.type = str

    @dataclass
    class SERVICE:
        type: str
        @dataclass
        class PROPERTIES:
            @dataclass
            class CANBOARDS:
                type: list[str]

                @dataclass
                class PROTOCOL:
                    major : list[int]
                    minor : list[int]
                @dataclass
                class FIRMWARE:
                    major: list[int]
                    minor: list[int]
                    build: list[int]
                PROTOCOL: PROTOCOL
                FIRMWARE: FIRMWARE
            @dataclass
            class SENSORS:
                id: list[str]
                framename: list[str]
                type: list[str]
                location: list[str]
            CANBOARDS: CANBOARDS
            SENSORS: SENSORS
        @dataclass
        class SETTINGS:
            acquisitionRate: int
            enabledSensors: list[str]
            temperature_acquisitionRate: int
        @dataclass
        class STRAIN_SETTINGS:
            useCalibration: bool
        PROPERTIES: PROPERTIES
        SETTINGS: SETTINGS
        STRAIN_SETTINGS: STRAIN_SETTINGS
    SERVICE: SERVICE

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