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
        attr = dict(Utils.parse_sysml(root_path+'/'+robot_name+'.sysml').part_definitions.items())
        robot = cls()

        # robot.version = attr['version']

        robot.parts = [Part.from_sysml(root_path, value) for key, value in attr.items()]
        return robot

    def to_xml(self, root_path, robot_name):
        attr = dict(Utils.parse_sysml(root_path+'/'+robot_name+'.sysml').part_definitions.items())
        override_values = []
        
        for key, value in attr.items():
            for part in self.parts:
                for override_key, override_value in value.parameters.items():
                    override_values.append((override_key, override_value))
                part.to_xml(root_path, "Head", robot_name, override_values)

        # with open(root_path+'/'+robot_name+'.sysml', 'r') as file:
        #     sysml_str = file.read()
        # override_pattern = r":>>\s*([a-zA-Z0-9._:(),\"= \-]+)\s*=\s*([a-zA-Z0-9._:(),\"= \-]+)\s*;"
        # subset_pattern = r'part (\w+) :> \w+ \{\s*([\s\S]*?)\}'

        # for match in re.findall(subset_pattern, sysml_str):
        #     override_matches = re.findall(override_pattern, match[1], re.DOTALL)
        #     for override_match in override_matches:
        # for part in self.parts:
            # part.to_xml(root_path, part.part_name.lower(), robot_name, override_matches)

def parse_args():
    parser = argparse.ArgumentParser(description="Generate XML files for robot parts")
    parser.add_argument("--robot", required=True, help="Path to the configuration files.")
    return parser.parse_args()

def main():
    robot_name = parse_args().robot
    robot = Robot.from_sysml('/home/mgloria/iit/study-alexandria/sysml/', robot_name)
    robot.to_xml('/home/mgloria/iit/study-alexandria/sysml/', robot_name)
    
if __name__ == '__main__':
    main()