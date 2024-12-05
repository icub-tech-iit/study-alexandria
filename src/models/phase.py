from dataclasses import dataclass
import re

@dataclass
class Phase:
    level: int
    type: str
    target: str

    @classmethod
    def from_sysml(cls, root_path, file_path):
        with open(root_path+file_path, 'r') as file:
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
    ph = Phase.from_sysml('/home/mgloria/iit/study-alexandria/sysml/','phase.sysml')
    print(ph)

if __name__ == '__main__':
    main()