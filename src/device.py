from dataclasses import dataclass
from utils import Utils

@dataclass
class Device:
    type: str
    name: str

    @classmethod
    def from_sysml(cls, root_path):
        attr = Utils.parse_sysml(root_path+'/device.sysml').part_definitions        
        attributes = {}

        for key, value in attr.items():
            for param in value.parameters:
                attributes[param] = value.parameters[param].strip('"')
        return cls(**attributes)
    
def main():
    pass

if __name__ == '__main__':
    main()