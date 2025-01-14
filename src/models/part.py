import re
import os
from utils import Utils
from calibrator import Calibrator as calibrator
from eln import Electronics as electronics
from mec import Mechanicals as mechanical 
from motorControl import motorControl
from mc_service import Service as service
from inertial import Inertial as inertial
from pc104 import PC104 as pc104
from pyparsing import nestedExpr

class Part:
    def __init__(self):
        self.part_name = str
        self.calibration = [calibrator]
        self.eln = [electronics]
        self.mechanicals = [mechanical]
        self.motorcontrol = [motorControl]
        self.service = [service]
        self.inertials = [inertial]
        self.pc104 = pc104

    @classmethod
    def from_sysml(cls, root_path, part):
        with open(root_path+'/'+part+'.sysml', 'r') as file:
            sysml_str = file.read()

        part = cls()
        part_pattern = r'part\s+(\w+)\s+\[(\d+)\]\s+:\>\s+(\w+)'
        parts_name_pattern = r'abstract part (\w+)'
        part_matches = re.findall(part_pattern, sysml_str)
        name_matches = re.findall(parts_name_pattern, sysml_str, re.DOTALL)

        override_pattern = r":>>\s*([a-zA-Z0-9._:(),\"= \-]+)\s*=\s*([a-zA-Z0-9._:(),\"= \-]+)\s*;"
        override_matches = re.findall(override_pattern, sysml_str, re.DOTALL) 

        part.part_name = name_matches[0]

        for match in part_matches:
            if match[2] == 'calibrator':
                part.calibration = [calibrator.from_sysml(root_path) for i in range(0, int(match[1]))]
            elif match[2] == 'electronics':
                part.eln = [electronics.from_sysml(root_path) for i in range(0, int(match[1]))]
            elif match[2] == 'mechanical':
                part.mechanicals = [mechanical.from_sysml(root_path) for i in range(0, int(match[1]))]
            elif match[2] == 'motorControl':
                part.motorcontrol = [motorControl.from_sysml(root_path) for i in range(0, int(match[1]))]
            elif match[2] == 'SERVICE':
                part.service = [service.from_sysml(root_path) for i in range(0, int(match[1]))]
            elif match[2] == 'inertial':
                part.inertials = [inertial.from_sysml(root_path) for i in range(0, int(match[1]))]
            elif match[2] == 'pc104':
                part.pc104 = pc104.from_sysml(root_path)
            else:
                print("No match found")
        return part

    def to_xml(self, root_path, part, robot_name):
        with open(root_path+'/'+part+'.sysml', 'r') as file:
            sysml_str = file.read()

        Utils.check_subfolders_existance(root_path, robot_name)
        robot_path = os.path.join(root_path, robot_name)

        override_pattern = r":>>\s*([a-zA-Z0-9._:(),\"= \-]+)\s*=\s*([a-zA-Z0-9._:(),\"= \-]+)\s*;"
        braces_patter = r"\{(.*?)\}"
        # override_matches = re.findall(override_pattern, sysml_str, re.DOTALL)
        # print(override_matches)
        subset_pattern = r'part (\w+) :> (\w+) = "([^"]+)" \{\s*([\s\S]*?)\}'

        # parts_pattern = r'abstract part (\w+)'
        # parts = re.findall(parts_pattern, sysml_str, re.DOTALL)

        for match in re.findall(subset_pattern, sysml_str):
            override_matches = re.findall(override_pattern, match[3], re.DOTALL)
            if match[1] == 'calibrator':
                for calib in self.calibration:
                    for ov in override_matches:
                        calib.update("calibrator."+"".join(ov[0].split()), ov[1])
                        calib.to_xml(robot_path, match[2])
            elif match[1] == 'eln':
                for electronics in self.eln:
                    electronics.to_xml(robot_path, match[2])
            elif match[1] == 'mechanical':
                for mechanical in self.mechanicals:
                    mechanical.to_xml(robot_path, match[2])
            elif match[1] == 'motorcontrol':
                for motorControl in self.motorcontrol:
                    motorControl.to_xml(robot_path, match[2])
            elif match[1] == 'service':
                for service in self.service:
                    service.to_xml(robot_path, match[2])
            elif match[1] == 'inertials':
                for inertial in self.inertials:
                    inertial.to_xml(robot_path, match[2])
            elif match[1] == 'pc104':
                self.pc104.to_xml(robot_path, match[2])
            else:
                print("No match found for part", match[1])

def main():
    part = Part.from_sysml('/home/mgloria/iit/study-alexandria/sysml', 'head')
    part.to_xml('/home/mgloria/iit/study-alexandria/sysml/', 'head', 'robot')
if __name__ == "__main__":
    main()
