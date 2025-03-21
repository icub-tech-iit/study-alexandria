import re
from lxml import etree
from dataclasses import dataclass
from utils import Utils

@dataclass
class PC104:
    PC104IpAddress: str
    PC104IpPort: int
    PC104TXrate: int
    PC104RXrate: int

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/pc104.sysml', 'r') as file:
            sysml_str = file.read()

        general_pattern = r'attribute (\w+) : \w+ default (?:(\d+(\.\d*)?)|"([^"]*)");' #catch integer/float with sign or quoted string

        matches = re.findall(general_pattern, sysml_str)
        attributes = {}
        for match in matches:
            key = match[0]
            value = None
            if match[1]:
                value = int(match[1])
            else:
                value = match[2] if match[3] is None else match[3]
            attributes[key] = value
        return cls(**attributes)
    
    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)
        
        Utils.check_subfolders_existance(root_path, file_name)

        group_elem = etree.SubElement(root, "group", {"name": self.__class__.__name__})
        for attr_name, attr_value in self.__dict__.items():
            param = etree.SubElement(group_elem, "param", {'name': attr_name})
            param.text = str(attr_value)
        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pc104 = PC104.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    pc104.to_xml('/home/mgloria/iit/study-alexandria/sysml')

if __name__ == '__main__':
    main()
