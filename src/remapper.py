from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from device import Device
from phase import Phase
from action import Action
from utils import parse_sysml, check_subfolders_existance

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
        attr = parse_sysml(root_path+'/templates/remapper.sysml').part_definitions
        remapper = cls(root_path)

        for key, value in attr.items():
            if hasattr(cls, key):
                subclass = getattr(cls, key)
                if is_dataclass(subclass):
                    params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                              for param, val in value.parameters.items()}
                    setattr(remapper, key, subclass(**params))
            elif key == 'remapper':
                remapper.folder_name = value.parameters['folder_name'].strip('"')
            elif key == 'startup':
                remapper.startup = Action.from_sysml(root_path)
            elif key == 'shutdown':
                remapper.shutdown = Phase.from_sysml(root_path)
        return remapper

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

        root.append(etree.XML(self.startup.to_xml()))
        root.append(etree.XML(self.shutdown.to_xml()))

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE devices PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()