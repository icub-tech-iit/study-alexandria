from dataclasses import dataclass
import re
import lxml.etree as etree

@dataclass
class Phase:
    level: int
    type: str
    target: str

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/phase.sysml', 'r') as file:
            sysml_str = file.read()

            patterns = {
                'level': r'attribute level : Integer default (\d+);',
                'type': r'attribute type : String default "([^"]+)";',
                'target': r'attribute target : String default "([^"]+)";',
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
    ph = Phase.from_sysml('/home/mgloria/iit/study-alexandria/sysml/')
    print(ph)
    # Phase.to_xml('/home/mgloria/iit/study-alexandria/sysml/')

if __name__ == '__main__':
    main()