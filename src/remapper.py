from lxml import etree
from dataclasses import dataclass
from device import Device
from phase import Phase
from action import Action
from utils import Utils

@dataclass
class Remapper(Device):
    elementName: list[str]
    elementValue: list[str]
    joints: int
    startup: Action
    shutdown: Phase    
    def __init__(self, root_path, **kwargs):
        self.folder_name = str
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.__dict__.update(kwargs)

    @classmethod
    def from_sysml(cls, root_path):
        attr = Utils.parse_sysml(root_path+'/remapper.sysml').part_definitions
        params = {}
        for key, value in attr.items():
            for param in value.parameters:
                params.update({param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                    for param, val in value.parameters.items()})
            if key == 'startup':
                params.update({key: Action.from_sysml(root_path)})
            elif key == 'shutdown':
                params.update({key: Phase.from_sysml(root_path)})
        return cls(root_path, **params)

    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': str(self.device_name).strip('"'), 'type': str(self.type).strip('"')}, nsmap=nsmap)
        
        Utils.check_subfolders_existance(root_path, file_name)

        paramlist = etree.SubElement(root, "paramlist", {'name': "networks"})
        if isinstance(self.elementName, str) and isinstance(self.elementValue, str):
            self.elementName = [self.elementName]
            self.elementValue = [self.elementValue]
        elementMap = dict(zip(self.elementName, self.elementValue))

        for elem_name, elem_value in elementMap.items():
            elem = etree.SubElement(paramlist, "elem", {'name': elem_name.strip('"')})
            elem.text = elem_value.strip('"')

        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, Action) or isinstance(attr_value, Phase) or attr_name in ['type', 'device_name', 'elementName', 'elementValue', 'folder_name']:
                continue
            else:
                param = etree.SubElement(root, "param", {"name": attr_name})
                param.text = str(attr_value)

        root.append(etree.XML(self.startup.to_xml()))
        root.append(etree.XML(self.shutdown.to_xml()))

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()