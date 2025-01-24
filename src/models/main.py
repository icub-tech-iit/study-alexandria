from part import Part
from utils import Utils
import re
import argparse


class Robot:
    def __init__(self):
        self.name = str
        self.version = str
        self.parts = [str]

    @classmethod
    def from_sysml(cls, root_path, robot_name):
        with open(root_path+'/'+robot_name+'.sysml', 'r') as file:
            sysml_str = file.read()

        general_pattern = r'attribute (\w+) : \w+ default (?:(\d+(\.\d*)?)|"([^"]*)");' #catch integer/float with sign or quoted string
        vector_pattern = r'attribute (\w+) :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);'
        override_pattern = r":>>\s*([a-zA-Z0-9._:(),\"= \-]+)\s*=\s*([a-zA-Z0-9._:(),\"= \-]+)\s*;"
        subset_pattern = r'(parts)\s*=\s*\((\w+)\)'
        
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
                
        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern) | extract_attributes(sysml_str, subset_pattern)
        robot.name = attr['name']
        robot.version = attr['version']
        robot.parts = [Part.from_sysml(root_path, i.strip().strip('"')) for i in attr['parts'].split(",")]
        return robot

    def to_xml(self, root_path, robot_name):
        with open(root_path+'/'+robot_name+'.sysml', 'r') as file:
            sysml_str = file.read()
        override_pattern = r":>>\s*([a-zA-Z0-9._:(),\"= \-]+)\s*=\s*([a-zA-Z0-9._:(),\"= \-]+)\s*;"
        subset_pattern = r'part (\w+) :> \w+ \{\s*([\s\S]*?)\}'

        for match in re.findall(subset_pattern, sysml_str):
            override_matches = re.findall(override_pattern, match[1], re.DOTALL)
            for override_match in override_matches:
                for part in self.parts:
                    part.to_xml(root_path, part.part_name.lower(), robot_name, override_matches)

def parse_args():
    parser = argparse.ArgumentParser(description="Generate XML files for robot parts")
    parser.add_argument("--robot", required=True, help="Path to the configuration files.")
    return parser.parse_args()

def main():
    robot_name = parse_args().robot
    robot = Robot.from_sysml('/home/mgloria/iit/study-alexandria/sysml', robot_name)
    robot.to_xml('/home/mgloria/iit/study-alexandria/sysml', robot_name)
    
if __name__ == '__main__':
    main()