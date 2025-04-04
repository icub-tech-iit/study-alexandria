from dataclasses import dataclass, is_dataclass, fields
from encoder import Encoder
from lxml import etree
from utils import Utils

class Service:
    def __init__(self, root_path):
        self.root_path = root_path
    @dataclass
    class SERVICE:
        type: list[str]
        @dataclass
        class PROPERTIES:
            @dataclass
            class ETHBOARD:
                type: str
            @dataclass
            class JOINTMAPPING:
                ENCODER1 = Encoder
                ENCODER2 = Encoder
                @dataclass
                class ACTUATOR:
                    type: list[str]
                    portName: list[str]
                ACTUATOR: ACTUATOR
            ETHBOARD: ETHBOARD
            JOINTMAPPING: JOINTMAPPING
        PROPERTIES: PROPERTIES
    SERVICE: SERVICE

    @classmethod
    def from_sysml(cls, root_path):
        attr = dict(reversed(Utils.parse_sysml(root_path+'/service.sysml').part_definitions.items()))
        service = cls(root_path)

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if key in ['ENCODER1', 'ENCODER2']:
                    setattr(instance, key, Encoder.from_sysml(root_path))
                elif hasattr(instance, key):
                    subclass = getattr(instance, key)
                    if is_dataclass(subclass):
                        params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                        setattr(instance, key, subclass(**params))
                    if value.children:
                        set_parameters(getattr(instance, key), {child: value.children[child] for child in value.children})
        set_parameters(service, attr)
        return service

    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)
        
        Utils.check_subfolders_existance(root_path, file_name)
        
        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.upper()})

            for field in fields(dataclass_instance):
                field_name = field.name
                field_value = getattr(dataclass_instance, field_name)
                if isinstance(field_value, Encoder):
                    group_elem.append(etree.XML(field_value.to_xml(field_name.upper())))
                elif is_dataclass(field_value):
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
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)
        
def main():
    pass

if __name__ == '__main__':
    main()