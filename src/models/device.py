from dataclasses import dataclass
import re

@dataclass
class Device:
    type: str
    name: str

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+"/device.sysml", 'r') as file:
            sysml_str = file.read()

            patterns = {
                'type': r'attribute type : String default "([^"]+)";',
                'name': r'attribute name : String default "([^"]+)";',
            }

            attributes = {}
            for key, pattern in patterns.items():
                match = re.search(pattern, sysml_str)
                if match:
                    attributes[key] = match.group(1)
                else:
                    raise ValueError(f"Pattern for {key} not found in the file")
            return cls(**attributes)

def main():
    dev = Device.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    print(dev)

if __name__ == '__main__':
    main()