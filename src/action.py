import lxml.etree as etree
from dataclasses import dataclass
from utils import Utils

@dataclass
class Action:
    phase: str
    level: int
    type: str
    elementName: list[str]
    elementValue: list[str]

    @classmethod
    def from_sysml(cls, root_path):
        attr = Utils.parse_sysml(root_path+'/templates/action.sysml').part_definitions    
        attributes = {}

        for key, value in attr.items():
            for param in value.parameters:
                if isinstance(value.parameters[param], dict):
                    attributes[param] = [x for x in value.parameters[param]['value'].strip("()").split(',')]
                else:
                    attributes[param] = value.parameters[param].strip('"')
        return cls(**attributes)
        
    def to_xml(self):
        root = etree.Element('action', {'phase': self.phase.strip('"'), "level": str(self.level).strip('"'), "type": self.type.strip('"')})
        paramlist = etree.SubElement(root, "paramlist", {'name': "networks"})
        if isinstance(self.elementName, str) and isinstance(self.elementValue, str):
            self.elementName = [self.elementName]
            self.elementValue = [self.elementValue]
        elementMap = dict(zip(self.elementName, self.elementValue))
        
        for elem_name, elem_value in elementMap.items():
            elem = etree.SubElement(paramlist, "elem", {'name': elem_name.strip('"')})
            elem.text = elem_value.strip('"')
        
        return etree.tostring(root, pretty_print=True)
    
def main():
    pass

if __name__ == '__main__':
    main()