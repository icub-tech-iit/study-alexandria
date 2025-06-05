from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from device import Device
from utils import parse_sysml, check_subfolders_existance

@dataclass
class FT(Device):
    type: str
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.includes = str
        self.folder_name = str

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
        attr = dict(reversed(parse_sysml(root_path+'/templates/ft.sysml').part_definitions.items()))
        ft_sensor = cls(root_path)

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if key == 'ft':
                    ft_sensor.includes = [include for include in value.parameters['includes']['value'].strip('()').split(',')]
                    ft_sensor.folder_name = value.parameters['folder_name'].strip('"')
                if hasattr(instance, key):
                    subclass = getattr(instance, key)
                    if is_dataclass(subclass):
                        params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                        setattr(instance, key, subclass(**params))
                    if value.children:
                        set_parameters(getattr(instance, key), {child: value.children[child] for child in value.children})

        set_parameters(ft_sensor, attr)
        return ft_sensor

    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self._generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()