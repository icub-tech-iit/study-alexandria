from dataclasses import dataclass
import re

@dataclass
class Phase:
    def __init__(self, level, type, target):
        self.level = level
        self.type = type
        self.target = target

    @classmethod
    def from_sysml(cls, file_path):
        with open(file_path, 'r') as file:
            sysml_str = file.read()

            level_pattern = r'attribute level : Integer = (\d+);'
            type_pattern = r'attribute type : String = "([^"]+)";'
            target_pattern = r'attribute target : String = "([^"]+)";'

            level_match = re.search(level_pattern, sysml_str)
            type_match = re.search(type_pattern, sysml_str)
            target_match = re.search(target_pattern, sysml_str)

            if level_match and type_match and target_match:
                level = int(level_match.group(1))
                type = str(type_match.group(1))
                target = str(target_match.group(1))
                return cls(level, type, target)
            else:
                raise ValueError("Invalid sysml file format")