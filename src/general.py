from lxml import etree
from dataclasses import dataclass
from utils import parse_sysml, check_subfolders_existance

@dataclass
class GENERAL:
    folder_name: str
    skipCalibration: bool
    useRawEncoderData: bool
    useLimitedPWM: bool
    verbose: bool

    @classmethod
    def from_sysml(cls, root_path):
        attr = parse_sysml(root_path+'/templates/general.sysml').part_definitions        
        attributes = {}

        for key, value in attr.items():
            for param in value.parameters:
                attributes[param] = value.parameters[param].strip('"')
        return cls(**attributes)
    
    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'portprefix': '', 'build': '1'}, nsmap=nsmap)
        check_subfolders_existance(root_path, file_name)

        group_elem = etree.SubElement(root, "group", {"name": self.__class__.__name__})
        for attr_name, attr_value in self.__dict__.items():
            if attr_name == 'folder_name':
                continue
            param = etree.SubElement(group_elem, "param", {'name': attr_name})
            param.text = str(attr_value)
        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass
if __name__ == '__main__':
    main()
