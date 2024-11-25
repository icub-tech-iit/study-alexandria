from dataclasses import dataclass
import re

@dataclass
class Encoder:
    type: list[str]
    port: list[str]
    position: list[str]
    resolution: list[int]
    tolerance: list[float]

    @classmethod
    def from_sysml(cls, file_path):
        with open(file_path, 'r') as file:
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
        
def main():
    enc = Encoder.from_sysml('/home/mgloria/iit/study-alexandria/sysml/encoder.sysml')
    print(enc.position)

if __name__ == '__main__':
    main()