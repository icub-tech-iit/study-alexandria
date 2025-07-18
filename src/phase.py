import lxml.etree as etree
from utils import parse_sysml

class Phase:
    def __init__(self):
        self.phase = str
        self.level = int
        self.type = str
        self.target = str

    @classmethod
    def from_sysml(cls, root_path):
        attr = parse_sysml(root_path+'/templates/phase.sysml').part_definitions        
        phase_class = cls()

        for key, value in attr.items():
            for param in value.parameters:
                setattr(phase_class, param, value.parameters[param].strip('"'))
        return phase_class  
        
    def to_xml(self):
        root = etree.Element('action', {'phase': self.phase.strip('"'), "level": str(self.level).strip('"'), "type": self.type.strip('"')})
        element = etree.SubElement(root, "param", {'name': "target"})
        element.text = self.target
        
        return etree.tostring(root, pretty_print=True)
    
def main():
    pass

if __name__ == '__main__':
    main()