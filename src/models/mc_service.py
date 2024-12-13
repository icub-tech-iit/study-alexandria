from dataclasses import dataclass, is_dataclass, asdict, fields
from encoder import Encoder
from lxml import etree
import re

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
                @dataclass
                class ACTUATOR:
                    type: list[str]
                    port: list[str]
                @dataclass
                class ENCODER1(Encoder):
                    def __init__(self):
                        encoder1 = Encoder().from_sysml(self.root_path)
                        super().__init__(**encoder1.__dict__)
                class ENCODER2(Encoder):
                    def __init__(self):
                        encoder2 = Encoder().from_sysml(self.root_path)
                        super().__init__(**encoder2.__dict__)
            
                actuator: ACTUATOR
                encoder1: ENCODER1
                encoder2: ENCODER2
            ethboard: ETHBOARD
            jointmapping: JOINTMAPPING
        properties: PROPERTIES
    service: SERVICE

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/service.sysml', 'r') as file:
            sysml_str = file.read()

        vector_pattern = r'attribute (\w+) :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);'
        enc_pattern = r'attribute (\w+) :> (\w+);'
        ser = cls(root_path)

        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            attributes = {}
            for match in matches:
                key = match[0]
                value = None
                if match[1]:
                    try:
                        value = float(match[1])
                    except ValueError:
                        value = match[1]
                elif match[2]:
                    value = int(match[2])
                else:
                    value = match[3]
                attributes[key] = value
            return attributes
                
        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, enc_pattern)
        
        ser.service = cls.SERVICE(
            type = attr['service_type'],
            properties = cls.SERVICE.PROPERTIES(
                ethboard = cls.SERVICE.PROPERTIES.ETHBOARD(
                    type = [attr['eth_type']]
                ),
                jointmapping = cls.SERVICE.PROPERTIES.JOINTMAPPING(
                    actuator = cls.SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR(
                        type = [attr['actuator_type']],
                        port = [attr['portName']]
                    ),
                    encoder1 = Encoder.from_sysml(root_path),
                    encoder2 = Encoder.from_sysml(root_path)
                )
            )
        )
        return ser

    def to_xml(self, root_path):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)
        
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
        with open(root_path + 'motorControl-service.xml', "wb") as writer:
            writer.write(xml_object)
        
def main():
    serv = Service('/home/mgloria/iit/study-alexandria/sysml').from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    serv.to_xml('/home/mgloria/iit/study-alexandria/sysml/')

if __name__ == '__main__':
    main()