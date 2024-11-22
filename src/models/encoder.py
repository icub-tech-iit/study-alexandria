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

            type_pattern = r'attribute type :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*(\d+);\s*:\s*>>\s*elements\s*:\s*(\w+)\[(\w+)\]\s*default\s*\(([^)]+)\);\s*}'
            port_pattern = r'attribute portName :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*(\d+);\s*:\s*>>\s*elements\s*:\s*(\w+)\[(\w+)\]\s*default\s*\(([^)]+)\);\s*}'
            position_pattern = r'attribute position :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*(\d+);\s*:\s*>>\s*elements\s*:\s*(\w+)\[(\w+)\]\s*default\s*\(([^)]+)\);\s*}'
            resolution_pattern = r'attribute resolution :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*(\d+);\s*:\s*>>\s*elements\s*:\s*(\w+)\[(\w+)\]\s*default\s*\(([^)]+)\);\s*}'
            tolerance_pattern = r'attribute tolerance :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*(\d+);\s*:\s*>>\s*elements\s*:\s*(\w+)\[(\w+)\]\s*default\s*\(([^)]+)\);\s*}'

            type_match = re.search(type_pattern, sysml_str)
            port_match = re.search(port_pattern, sysml_str)
            position_match = re.search(position_pattern, sysml_str)
            resolution_match = re.search(resolution_pattern, sysml_str)
            tolerance_match = re.search(tolerance_pattern, sysml_str)

            if type_match and port_match and position_match and resolution_match and tolerance_match:
                type = type_match.group(4)
                port = port_match.group(4)
                position = position_match.group(4)
                resolution = (resolution_match.group(4))
                tolerance = (tolerance_match.group(4))
                return cls(type, port, position, resolution, tolerance)
            else:
                raise ValueError("Pattern not found in the file")