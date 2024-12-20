from dataclasses import dataclass
import re
from lxml import etree

@dataclass
class Encoder:
    type: list[str]
    port: list[str]
    position: list[str]
    resolution: list[int]
    tolerance: list[float]

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/encoder.sysml', 'r') as file:
            sysml_str = file.read()

        patterns = {
            'type': r'attribute type :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);\s*}',
            'port': r'attribute portName :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);\s*}',
            'position': r'attribute position :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);\s*}',
            'resolution': r'attribute resolution :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);\s*}',
            'tolerance': r'attribute tolerance :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);\s*}'
        }

        attributes = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, sysml_str)
            if match:
                attributes[key] = match.group(1)
            else:
                raise ValueError(f"Pattern for {key} not found in the file")

        return cls(**attributes)
        
    def to_xml(self, encoder_name=None):
        encoder_name = self.__class__.__name__ if encoder_name is None else encoder_name
        group_elem = etree.Element("group", {"name": encoder_name})
        for attr_name, attr_value in self.__dict__.items():
            param = etree.SubElement(group_elem, "param", {'name': attr_name})
            param.text = str(attr_value)
        etree.indent(group_elem, space='    ')
        
        return etree.tostring(group_elem, pretty_print=True)

def main():
    enc = Encoder.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    # enc.to_xml('/home/mgloria/iit/study-alexandria/sysml')

if __name__ == '__main__':
    main()