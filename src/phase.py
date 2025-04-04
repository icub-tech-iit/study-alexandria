import lxml.etree as etree
from dataclasses import dataclass
from utils import Utils

@dataclass
class Phase:
    phase: str
    level: int
    type: str
    target: str

    @classmethod
    def from_sysml(cls, root_path):
        attr = Utils.parse_sysml(root_path+'/phase.sysml').part_definitions        
        attributes = {}

        for key, value in attr.items():
            for param in value.parameters:
                attributes[param] = value.parameters[param].strip('"')
        return cls(**attributes)
        
    def to_xml(self):
        root = etree.Element('action', {'phase': self.phase.strip('"'), "level": self.level, "type": self.type.strip('"')})
        element = etree.SubElement(root, "param", {'name': "target"})
        element.text = self.target
        
        return etree.tostring(root, pretty_print=True)
    
def main():
    pass

if __name__ == '__main__':
    main()