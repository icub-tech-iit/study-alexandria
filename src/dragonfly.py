from lxml import etree
from dataclasses import dataclass, field, is_dataclass
from device import Device
from utils import Utils

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
        attr = dict(reversed(Utils.parse_sysml(root_path + '/dragonfly.sysml').part_definitions.items()))

        for key, value in attr.items():
            for param in value.parameters:
                params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                    for param, val in value.parameters.items()}
        return cls(root_path, **params)

    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': str(self.device_name).strip('"'), 'type': str(self.type).strip('"')}, nsmap=nsmap)
        
        Utils.check_subfolders_existance(root_path, file_name)

        for attr_name, attr_value in self.__dict__.items():
            if attr_name in ['type', 'device_name', 'folder_name']: #TODO: fix to skip Device class members
                continue
            param = etree.SubElement(root, "param", {'name': attr_name})
            param.text = str(attr_value)
        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()