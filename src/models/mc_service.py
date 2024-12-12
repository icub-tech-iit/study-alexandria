from dataclasses import dataclass, is_dataclass, asdict, fields
from encoder import Encoder
from lxml import etree
import re

@dataclass
class SERVICE:
    def __init__(self, root_path):
        self.root_path = root_path
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
        ser.type = attr['service_type']

        ser.properties = cls.PROPERTIES()
        ser.ethboard = cls.PROPERTIES().ETHBOARD(
            type = [attr['eth_type']]
        )

        ser.jointmapping = cls.PROPERTIES().JOINTMAPPING()
        ser.actuator = cls.PROPERTIES().JOINTMAPPING().ACTUATOR(
            type = [attr['actuator_type']],
            port = [attr['portName']]
        )

        ser.encoder1 = Encoder.from_sysml(root_path)
        ser.encoder2 = Encoder.from_sysml(root_path)
        return ser
    
    def to_xml(self, root_path):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)

        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.upper()})
            for field_name, field_value in asdict(dataclass_instance).items():
                if fields(dataclass_instance):
                    param = etree.SubElement(group_elem, "param", {"name": field_name})
                    param.text = " ".join(map(str, field_value)) if isinstance(field_value, list) else str(field_value)                    
                else:
                    _dataclass_to_xml(group_elem, field_name, field_value)
        for attr_name, attr_value in self.__dict__.items():
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        # Write to file
        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path + 'motorControl-service.xml', "wb") as writer:
            writer.write(xml_object)
    
def main():
    serv = SERVICE('/home/mgloria/iit/study-alexandria/sysml').from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    serv.to_xml('/home/mgloria/iit/study-alexandria/sysml/')
    print(serv.encoder2.position)

if __name__ == '__main__':
    main()