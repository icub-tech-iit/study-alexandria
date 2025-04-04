from dataclasses import dataclass
from utils import Utils
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
        attr = dict(reversed(Utils.parse_sysml(root_path+'/encoder.sysml').part_definitions.items()))     
        attributes = {}

        for key, value in attr.items():
            for param in value.parameters:
                params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
        return cls(**params)
        
    def to_xml(self, encoder_name=None):
        encoder_name = self.__class__.__name__ if encoder_name is None else encoder_name
        group_elem = etree.Element("group", {"name": encoder_name})
        for attr_name, attr_value in self.__dict__.items():
            param = etree.SubElement(group_elem, "param", {'name': attr_name})
            param.text = str(attr_value)
        etree.indent(group_elem, space='    ')
        
        return etree.tostring(group_elem, pretty_print=True)

def main():
    pass

if __name__ == '__main__':
    main()