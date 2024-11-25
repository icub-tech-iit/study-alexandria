from dataclasses import dataclass
from encoder import Encoder
import re

@dataclass
class SERVICE:
    type: list[str]
    class PROPERTIES:
        @dataclass
        class ETHBOARD:
            type: str
        class JOINTMAPPING:
            @dataclass
            class ACTUATOR:
                type: list[str]
                port: list[str]
            class ENCODER1(Encoder):
                def __init__(self):
                    encoder1 = Encoder().from_sysml('/home/mgloria/iit/study-alexandria/sysml/encoder.sysml')
                    super().__init__(**encoder1.__dict__)
            class ENCODER2(Encoder):
                def __init__(self):
                    encoder2 = Encoder().from_sysml('/home/mgloria/iit/study-alexandria/sysml/encoder.sysml')
                    super().__init__(**encoder2.__dict__)
        
    @classmethod
    def from_sysml(cls, file_path):
        with open(file_path, 'r') as file:
            sysml_str = file.read()

        patterns = {
            'type': r'attribute type :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);\s*}',
            'portName': r'attribute portName :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);\s*}',
        }

        block_patterns = {
            # 'SERVICE': r'part SERVICE {([^}]*)}',
            'PROPERTIES': r'part PROPERTIES {([^}]*)}',
            'ETHBOARD': r'part ETHBOARD {([^}]*)}',
            'JOINTMAPPING': r'part JOINTMAPPING {([^}]*)}',
            'ACTUATOR': r'part ACTUATOR {([^}]*)}',
        }

        attributes = {}
        parts = {}
        for key_block, pattern_block in block_patterns.items():
            match_block = re.search(pattern_block, sysml_str)
            if match_block:
                parts[key_block] = match_block.group(1)

        # Extract attributes within each part
        for part_name, part_content in parts.items():
            attributes[part_name] = {}
            for key, pattern in patterns.items():
                match = re.search(pattern, part_content)
                if match:
                    attributes[part_name][key] = match.group(1)
                    print(attributes)
                else:
                    raise ValueError(f"Pattern for {key} not found in the part {part_name}")
                        
        # return cls(**parts)
                # match = re.search(pattern, sysml_str)
                # if match:
                #     attributes[key] = match.group(1)
                # else:
                #     raise ValueError(f"Pattern for {key} not found in the file")

            # return cls(**parts)
        
def main():
    serv = SERVICE.from_sysml('/home/mgloria/iit/study-alexandria/sysml/service.sysml')
    print(serv)

if __name__ == '__main__':
    main()