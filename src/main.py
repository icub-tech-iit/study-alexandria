from part import Part
from utils import Utils
import argparse


class Robot:
    def __init__(self):
        self.name = str
        self.version = str
        self.parts = [str]

    @classmethod
    def from_sysml(cls, root_path, robot_name):
        attr = dict(Utils.parse_sysml(root_path+'/robots/'+robot_name+'.sysml').part_definitions.items())
        robot = cls()

        robot.parts = [Part.from_sysml(root_path, key) for key, value in attr.items()]
        return robot

    def to_xml(self, root_path, robot_name):
        attr = dict(Utils.parse_sysml(root_path+'/robots/'+robot_name+'.sysml').part_definitions.items())
        override_values = []
        
        for key, value in attr.items():
            for part in self.parts:
                for override_key, override_value in value.parameters.items():
                    override_values.append((override_key, override_value))
                part.to_xml(root_path, key, robot_name, override_values)

def parse_args():
    parser = argparse.ArgumentParser(description="Generate XML files for the specified robot")
    parser.add_argument("--robot", required=True, nargs='+', help="Names of the robots (space-separated list).")
    parser.add_argument("--config", required=True, help="Absolute path to the SysML file.")
    return parser.parse_args()

def main():
    robots_name = parse_args().robot
    sysml_path = parse_args().config
    for robot_name in robots_name:
        try:
            robot = Robot.from_sysml(sysml_path, robot_name)
            robot.to_xml(sysml_path, robot_name)
        except FileNotFoundError as e:
            print(f"File not found for {robot_name}: {e}")
            continue
    
if __name__ == '__main__':
    main()