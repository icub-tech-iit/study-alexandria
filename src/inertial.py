from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from device import Device
from utils import Utils

class Inertial(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.type = str
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
                sensorName: list[str]
                type: list[str]
                boardType: list[str]
                location: list[str]
            CANBOARDS: CANBOARDS
            SENSORS: SENSORS
        @dataclass
        class SETTINGS:
            acquisitionRate: int
            enabledSensors: list[str]
        PROPERTIES: PROPERTIES
        SETTINGS: SETTINGS
    SERVICE: SERVICE

    @classmethod
    def from_sysml(cls, root_path):
        attr = dict(reversed(Utils.parse_sysml(root_path+'/inertial.sysml').part_definitions.items()))
        inertial = cls(root_path)

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if key == 'inertial':
                    inertial.includes = [include for include in value.parameters['includes']['value'].strip('()').split(',')]
                    inertial.folder_name = value.parameters['folder_name'].strip('"')
                if hasattr(instance, key):
                    subclass = getattr(instance, key)
                    if is_dataclass(subclass):
                        params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                        setattr(instance, key, subclass(**params))
                    if value.children:
                        set_parameters(getattr(instance, key), {child: value.children[child] for child in value.children})

        set_parameters(inertial, attr)
        return inertial

    def to_xml(self, root_path, file_name):
        xi_ns = 'http://www.w3.org/2001/XInclude'
        nsmap = {'xi': xi_ns}
        root = etree.Element('device', {'name': str(self.name).strip('"'), 'type': str(self.type).strip('"')}, nsmap=nsmap)
        
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
            if attr_name == 'includes':
                for include in attr_value:
                    etree.SubElement(root, f'{{{xi_ns}}}include', href=include.strip('"'))
            if attr_name == 'folder_name':
                continue
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+"/"+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()