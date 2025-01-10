import re
from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from device import Device
from utils import Utils

class Inertial(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
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

                protocol: PROTOCOL
                firmware: FIRMWARE

            @dataclass
            class SENSORS:
                id: list[str]
                type: list[str]
                boardType: list[str]
                location: list[str]
            @dataclass
            class SETTINGS:
                acquisitionRate: int
                enabledSensors: list[str]
            canboards: CANBOARDS
            sensors: SENSORS
            settings: SETTINGS
        properties: PROPERTIES
    service: SERVICE

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/inertial.sysml', 'r') as file:
            sysml_str = file.read()
    
        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            attributes = {}
            for match in matches:
                key = match[0]
                value = None
                if match[1]:
                    try:
                        value = float(match[1]) if isinstance(match[1], float) else int(match[1])
                    except ValueError:
                        value = match[1]
                elif match[2]:
                    value = int(match[2])
                else:
                    value = match[3]
                attributes[key] = value
            return attributes
        
        general_pattern = r'attribute (\w+) : \w+ default (?:(\d+(\.\d*)?)|"([^"]*)");' #catch integer/float with sign or quoted string
        vector_pattern = r'attribute (\w+) :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);'

        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern)
        inertial = cls(root_path)

        inertial.type = attr['type']
        inertial.service = cls.SERVICE(
            type = attr['serv_type'],
            properties = cls.SERVICE.PROPERTIES(
                canboards = cls.SERVICE.PROPERTIES.CANBOARDS(
                    type = [item.strip() for item in attr['type'].split(",")],
                    protocol = cls.SERVICE.PROPERTIES.CANBOARDS.PROTOCOL(
                        major = [attr['major']],
                        minor = [attr['minor']],
                    ),
                    firmware = cls.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE(
                        major = [attr['major']],
                        minor = [attr['minor']],
                        build = [attr['build']]
                    )
                ),
                sensors = cls.SERVICE.PROPERTIES.SENSORS(
                    id = [item.strip() for item in attr['id'].split(",")],
                    type = [item.strip() for item in attr['type'].split(",")],
                    boardType = [item.strip() for item in attr['boardType'].split(",")],
                    location = [item.strip() for item in attr['location'].split(",")]
                ),
                settings = cls.SERVICE.PROPERTIES.SETTINGS(
                    acquisitionRate = attr['acquisitionRate'],
                    enabledSensors = [item.strip() for item in attr['enabledSensors'].split(",")]
                )
            )
        )
        cls.type = attr['serv_type']
        return inertial

    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': ' ', 'type': 'device_type'}, nsmap=nsmap)
        
        Utils.check_subfolders_existance(root_path, file_name)

        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.upper()})

            for field in fields(dataclass_instance):
                field_name = field.name
                field_value = getattr(dataclass_instance, field_name)
                
                if is_dataclass(field_value):
                    _dataclass_to_xml(group_elem, field_name, field_value) 
                elif isinstance(field_value, list):
                    if any(isinstance(i, list) for i in field_value):
                        param = etree.SubElement(group_elem, "param", {"name": field_name})
                        formatted_text = "\n".join(
                            "   ".join(map(str, row)) for row in field_value
                        )
                        param.text = f"\n{formatted_text}\n"
                    else:
                        param = etree.SubElement(group_elem, "param", {"name": field_name})
                        param.text = "   ".join(map(str, field_value))
                else:
                    param = etree.SubElement(group_elem, "param", {"name": field_name})
                    param.text = str(field_value)

        for attr_name, attr_value in self.__dict__.items():
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+"/"+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    root_path = "/home/mgloria/iit/study-alexandria/sysml/"
    inertial = Inertial(root_path).from_sysml(root_path)
    inertial.to_xml(root_path, "inertial.xml")
if __name__ == "__main__":
    main()