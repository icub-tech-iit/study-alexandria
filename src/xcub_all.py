from utils import parse_sysml, check_subfolders_existance
from lxml import etree

class Xcub_all:
    def __init__(self, root_path):
        self.folder_name = str
        self.pc104 = str
        self.cartesian = []
        self.motorControl_wrapper = []
        self.motorControl_remapper = []
        self.motorControl = []
        self.FT = []
        self.calibrators = []

    @classmethod
    def from_sysml(cls, root_path):
        attr = parse_sysml(root_path + '/templates/xcub_all.sysml').part_definitions
        all_instance = cls(root_path)

        for key, value in attr.items():
            for name, param in value.parameters.items():
                if name == 'folder_name':
                    all_instance.folder_name = value.parameters['folder_name'].strip('"')
                if isinstance(param, dict) and 'value' in param:
                    array_value = param['value'].strip("()").split(',')
                    cleaned_values = [x.strip('"') for x in array_value if x.strip()]
                    setattr(all_instance, name, cleaned_values)
                else:
                    setattr(all_instance, name, param)
        return all_instance
    
    def to_xml(self, root_path, file_name):
        xi_ns = 'http://www.w3.org/2001/XInclude'
        nsmap = {'xi': xi_ns}
        root = etree.Element('robot', {'name': '', 'portprefix': '', 'build': "1"}, nsmap=nsmap)

        check_subfolders_existance(root_path, file_name)
        param = etree.SubElement(root, "params")
        device = etree.SubElement(root, "devices")
        for attr_name, attr_value in self.__dict__.items():
            if attr_name == 'folder_name':
                continue
            for attr in attr_value:
                if attr_name == 'pc104':
                    etree.SubElement(param, f'{{{xi_ns}}}include', href=attr)
                else:
                    etree.SubElement(device, f'{{{xi_ns}}}include', href=attr)

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE robot PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+"/"+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()