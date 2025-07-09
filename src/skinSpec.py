from dataclasses import dataclass, is_dataclass, fields
from lxml import etree
from utils import Utils
class skinSpec:
    def __init__(self):
        self.folder_name = str
    @dataclass
    class defaultCfgBoard:
        period: int
        skinType: int
        noLoad: str
        diagnostic: bool
    @dataclass
    class defaultCfgTriangle:
        enabled: bool
        shift: int
        cdcOffset: str
    @dataclass
    class specialCfgTriangles:
        numOfSets: int
        triangleSetCfg1: list[int]
        triangleSetCfg2: list[int]
        triangleSetCfg3: list[int]
        triangleSetCfg4: list[int]
        triangleSetCfg5: list[int]
        triangleSetCfg6: list[int]
        triangleSetCfg7: list[int]
        triangleSetCfg8: list[int]
        triangleSetCfg9: list[int]
        triangleSetCfg10: list[int]
        triangleSetCfg11: list[int]
        triangleSetCfg12: list[int]
        triangleSetCfg13: list[int]
        triangleSetCfg14: list[int]
        triangleSetCfg15: list[int]
        triangleSetCfg16: list[int]
        triangleSetCfg17: list[int]
        triangleSetCfg18: list[int]
        triangleSetCfg19: list[int]
        triangleSetCfg20: list[int]

    @classmethod
    def from_sysml(cls, root_path):
        attr = dict(Utils.parse_sysml(root_path+'/templates/skinSpec.sysml').part_definitions.items())
        skinSpec = cls()

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if hasattr(instance, key):
                    subclass = getattr(instance, key)
                    if is_dataclass(subclass):
                        params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                        setattr(instance, key, subclass(**params))
                    if value.children:
                        set_parameters(getattr(instance, key), {child: value.children[child] for child in value.children})
                if key == 'skinSpec':
                    skinSpec.folder_name = value.parameters['folder_name'].strip('"')
        set_parameters(skinSpec, attr)
        return skinSpec
    
    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)
        
        Utils.check_subfolders_existance(root_path, file_name)
        
        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name})

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
            if attr_name == 'folder_name':
                continue
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()