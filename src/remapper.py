from lxml import etree
from dataclasses import fields
from device import Device
from phase import Phase
from action import Action
from utils import check_subfolders_existance

class Remapper(Device):   
    def __init__(self, root_path, **kwargs):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)

        self.elementName = list[str]
        self.elementValue = list[str]
        self.joints = int
        self.startup = Action
        self.shutdown = Phase

    @classmethod
    def from_sysml(cls, root_path):
        return super().from_sysml(root_path)

    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': str(self.device_name).strip('"'), 'type': str(self.type).strip('"')}, nsmap=nsmap)
        
        check_subfolders_existance(root_path, file_name)

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
        
        extra_attrs = [self.startup, self.shutdown]
        for attr in extra_attrs:
            root.append(super()._extra_attributes(attr))

        self.generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()