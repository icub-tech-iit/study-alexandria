from part import Part
from dataclasses import dataclass
import re

class Robot:
    def __init__(self):
        self.name = str
        self.version = str
        self.parts = list[Part]

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/iCubErzelli03.sysml', 'r') as file:
            sysml_str = file.read()

        general_pattern = r'attribute (\w+) : \w+ default (?:(\d+(\.\d*)?)|"([^"]*)");' #catch integer/float with sign or quoted string
        vector_pattern = r'attribute (\w+) :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);'
        robot = cls()
        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            attributes = {}
            for match in matches:
                key = match[0]
                value = None
                if match[1]:
                    try:
                        value = float(match[1]) if isinstance(match[1], float) else int(match[1])
                    except ValueError:
                        value = match[1]
                elif match[2]:
                    value = int(match[2])
                else:
                    value = match[3]
                attributes[key] = value
            return attributes
                
        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern)
        robot.name = attr['name']
        robot.version = attr['version']
        robot.parts = [Part.from_sysml(root_path, i.strip().strip('"')) for i in attr['parts'].split(",")]
        return robot

    def to_xml(self, root_path, robot_name):
        for part in self.parts:
            part.to_xml(root_path, part.part_name, robot_name)

def main():
    robot = Robot.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    robot.to_xml('/home/mgloria/iit/study-alexandria/sysml', robot.name)
    
if __name__ == '__main__':
    main()