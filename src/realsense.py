from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from device import Device
from utils import parse_sysml, check_subfolders_existance

class Realsense(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.folder_name = str

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
        attr = dict(parse_sysml(root_path+'/templates/realsense.sysml').part_definitions.items())
        realsense_camera = cls(root_path)

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if hasattr(instance, key):
                    subclass = getattr(instance, key)
                    if is_dataclass(subclass):
                        params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                        setattr(instance, key, subclass(**params))
                    if value.children:
                        set_parameters(getattr(instance, key), {child: value.children[child] for child in value.children})
                if key == 'realsense':
                    realsense_camera.folder_name = value.parameters['folder_name'].strip('"')

        set_parameters(realsense_camera, attr)
        return realsense_camera

    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self._generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()