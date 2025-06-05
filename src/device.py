from dataclasses import dataclass
from utils import parse_sysml
from lxml import etree
from utils import check_subfolders_existance
from dataclasses import fields, is_dataclass
from phase import Phase
from action import Action

@dataclass
class Device:
    type: str
    device_name: str

    @classmethod
    def from_sysml(cls, root_path):
        attr = parse_sysml(root_path+'/templates/device.sysml').part_definitions        
        attributes = {}

        for key, value in attr.items():
            for param in value.parameters:
                attributes[param] = value.parameters[param].strip('"')
        return cls(**attributes)
    
    def to_xml(self, root_path, file_name):
        root, xi_ns = self._define_root()
        check_subfolders_existance(root_path, file_name)

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
            if self._skip_cases(attr_name) or isinstance(attr_value, Phase) or isinstance(attr_value, Action):
                continue
            elif attr_name == 'includes':	
                self._add_includes(attr_value, root)
            elif is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)
            else:
                param = etree.SubElement(root, "param", {"name": attr_name})
                param.text = "".join(map(str, attr_value)) if isinstance(attr_value, list) else str(attr_value)

        return root
    
    def _skip_cases(self, attr_name):
        return attr_name in ['type', 'device_name', 'folder_name']

    def _add_includes(self, includes, root):
        xi_ns = 'http://www.w3.org/2001/XInclude'
        if isinstance(includes, list):
            return [etree.SubElement(root, f'{{{xi_ns}}}include', href=inc) for inc in includes]
        else:
            return etree.SubElement(root, f'{{{xi_ns}}}include', href=includes)    
    def _extra_attributes(self, extra_attr):
        return etree.XML(extra_attr.to_xml())
    
    def _define_root(self):
        xi_ns = 'http://www.w3.org/2001/XInclude'
        nsmap = {'xi': xi_ns}
        root = etree.Element('device', {'name': str(self.device_name).strip('"'), 'type': str(self.type).strip('"')}, nsmap=nsmap)
        return root, xi_ns
    
    def _generate_xml(self, root, root_path, file_name):
        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE devices PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+"/"+file_name, "wb") as writer:
            writer.write(xml_object)
    
def main():
    pass

if __name__ == '__main__':
    main()