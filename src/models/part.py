import re
import os
from utils import Utils
from calibrator import Calibrator as calibrator
from eln import Electronics as electronics
from mec import Mechanicals as mechanicals 
from motorControl import motorControl
from mc_service import Service as service
from inertial import Inertial as inertial
from pc104 import PC104 as pc104
from utils import Utils
class Part:
    def __init__(self):
        self.part_name = str
        self.calibration = [calibrator]
        self.eln = [electronics]
        self.mechanicals = [mechanicals]
        self.motorcontrol = [motorControl]
        self.service = [service]
        self.inertials = [inertial]
        self.pc104 = pc104

    @classmethod
    def from_sysml(cls, root_path, part):
        with open(root_path+'/'+part+'.sysml', 'r') as file:
            sysml_str = file.read()

        part = cls()
        part_pattern = r'part (\w+) \[(\d+)\] ='
        parts_name_pattern = r'abstract part (\w+)'
        part_matches = re.findall(part_pattern, sysml_str)
        name_matches = re.findall(parts_name_pattern, sysml_str, re.DOTALL)
        # override_pattern = r":>>\s*([a-zA-Z0-9._:(),\"= \-]+)\s*=\s*([a-zA-Z0-9._:(),\"= \-]+)\s*;"
        # override_matches = re.findall(override_pattern, sysml_str, re.DOTALL) 
        subset_pattern = r'part (\w+) :> (\w+) = "([^"]+)" \{\s*([\s\S]*?)\}'
        subset_matches = re.findall(subset_pattern, sysml_str, re.DOTALL)

        part.part_name = name_matches[0]

        calibrators = []
        elns = []
        pc104s = []
        mechs = []
        mc = []
        services = []

        for match in subset_matches:
            if match[1] == 'calibrator':
                calibrators.append(match[0])
            elif match[1] == 'electronics':
                elns.append(match[0])
            elif match[1] == 'PC104':
                pc104s.append(match[0])
            elif match[1] == 'mechanical':
                mechs.append(match[0])
            elif match[1] == 'motorControl':
                mc.append(match[0])
            elif match[1] == 'SERVICE':
                services.append(match[0])
            else:
                print("No match found for part", match[1])
            part.calibration = [calibrator.from_sysml(root_path) for i in calibrators]
            part.eln = [electronics.from_sysml(root_path) for i in elns]
            part.pc104 = pc104.from_sysml(root_path)
            part.mechanicals = [mechanicals.from_sysml(root_path) for i in mechs]
            part.motorcontrol = [motorControl.from_sysml(root_path) for i in mc]
            part.service = [service.from_sysml(root_path) for i in services]
        return part

    def to_xml(self, root_path, part, robot_name):
        with open(root_path+'/'+part+'.sysml', 'r') as file:
            sysml_str = file.read()

        Utils.check_subfolders_existance(root_path, robot_name)
        robot_path = os.path.join(root_path, robot_name)

        override_pattern = r":>>\s*([a-zA-Z0-9._:(),\"= \-]+)\s*=\s*([a-zA-Z0-9._:(),\"= \-]+)\s*;"
        subset_pattern = r'part (\w+) :> (\w+) = "([^"]+)" \{\s*([\s\S]*?)\}'
        
        for match in re.findall(subset_pattern, sysml_str):
            override_matches = re.findall(override_pattern, match[3], re.DOTALL)
            if match[1] == 'calibrator':
                for calib in self.calibration:
                    for override_match in override_matches:
                        Utils.update(calib, "calibrator." + "".join(override_match[0].split()), override_match[1])
                    calib.to_xml(robot_path, match[2])
            elif match[1] == 'electronics':
                for electronic in self.eln:
                    for override_match in override_matches:
                        Utils.update(electronic, "electronics." + "".join(override_match[0].split()), override_match[1])
                    electronic.to_xml(robot_path, match[2])
            elif match[1] == 'mechanical':
                for mech in self.mechanicals:
                    for override_match in override_matches:
                        Utils.update(mech, "mechanicals." + "".join(override_match[0].split()), override_match[1])
                    mech.to_xml(robot_path, match[2])
            elif match[1] == 'motorControl':
                for motorControl in self.motorcontrol:
                    for override_match in override_matches:
                        Utils.update(motorControl, "motorControl." + "".join(override_match[0].split()), override_match[1])
                    motorControl.to_xml(robot_path, match[2])
            elif match[1] == 'SERVICE':
                for service in self.service:
                    for override_match in override_matches:
                        Utils.update(service, "SERVICE." + "".join(override_match[0].split()), override_match[1])
                    service.to_xml(robot_path, match[2])
            elif match[1] == 'inertials':
                for inertial in self.inertials:
                    for override_match in override_matches:
                        Utils.update(inertial, "inertials." + "".join(override_match[0].split()), override_match[1])
                    inertial.to_xml(robot_path, match[2])
            elif match[1] == 'PC104':
                self.pc104.to_xml(robot_path, match[2])
            else:
                print("No match found for part", match[1])


def main():
    part = Part.from_sysml('/home/mgloria/iit/study-alexandria/sysml', 'head')
    part.to_xml('/home/mgloria/iit/study-alexandria/sysml/', 'head', 'robot')
if __name__ == "__main__":
    main()
