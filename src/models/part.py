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
        parts_name_pattern = r'abstract part (\w+)'
        name_matches = re.findall(parts_name_pattern, sysml_str, re.DOTALL)
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
            elif match[1] == 'service':
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

    def to_xml(self, root_path, part, robot_name, overr_params):
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
                    specific_overrides = [
                        (override_key.split('.', 1)[1], override_value)
                        for override_key, override_value in overr_params
                        if override_key.split('.', 1)[0] == match[0]
                    ]
                    combined_overrides = override_matches + specific_overrides
                    for override_match in combined_overrides:
                        if isinstance(override_match, tuple) and len(override_match) == 2:
                            override_key = override_match[0].strip()
                            override_value = override_match[1].strip()
                            Utils.update(calib, f"calibrator.{override_key}", override_value)
                    calib.to_xml(robot_path, match[2])
            elif match[1] == 'electronics':
                for electronic in self.eln:
                    specific_overrides = [
                        (override_key.split('.', 1)[1], override_value)
                        for override_key, override_value in overr_params
                        if override_key.split('.', 1)[0] == match[0]
                    ]
                    combined_overrides = override_matches + specific_overrides
                    for override_match in combined_overrides:
                        if isinstance(override_match, tuple) and len(override_match) == 2:
                            override_key = override_match[0].strip()
                            override_value = override_match[1].strip()
                            Utils.update(electronic, f"electronics.{override_key}", override_value)
                    electronic.to_xml(robot_path, match[2])
            elif match[1] == 'mechanical':
                for mech in self.mechanicals:
                    specific_overrides = [
                        (override_key.split('.', 1)[1], override_value)
                        for override_key, override_value in overr_params
                        if override_key.split('.', 1)[0] == match[0]
                    ]
                    combined_overrides = override_matches + specific_overrides
                    for override_match in combined_overrides:
                        if isinstance(override_match, tuple) and len(override_match) == 2:
                            override_key = override_match[0].strip()
                            override_value = override_match[1].strip()
                            Utils.update(mech, f"mechanicals.{override_key}", override_value)
                    mech.to_xml(robot_path, match[2])
            elif match[1] == 'motorControl':
                for motorControl in self.motorcontrol:
                    specific_overrides = [
                        (override_key.split('.', 1)[1], override_value)
                        for override_key, override_value in overr_params
                        if override_key.split('.', 1)[0] == match[0]
                    ]
                    combined_overrides = override_matches + specific_overrides
                    for override_match in combined_overrides:
                        if isinstance(override_match, tuple) and len(override_match) == 2:
                            override_key = override_match[0].strip()
                            override_value = override_match[1].strip()
                            Utils.update(motorControl, f"motorControl.{override_key}", override_value)
                    motorControl.to_xml(robot_path, match[2])
            elif match[1] == 'service':
                for service in self.service:
                    specific_overrides = [
                        (override_key.split('.', 1)[1], override_value)
                        for override_key, override_value in overr_params
                        if override_key.split('.', 1)[0] == match[0]
                    ]
                    combined_overrides = override_matches + specific_overrides
                    for override_match in combined_overrides:
                        if isinstance(override_match, tuple) and len(override_match) == 2:
                            override_key = override_match[0].strip()
                            override_value = override_match[1].strip()
                            Utils.update(service, f"SERVICE.{override_key}", override_value)
                    service.to_xml(robot_path, match[2])
            elif match[1] == 'inertials':
                for inertial in self.inertials:
                    specific_overrides = [
                        (override_key.split('.', 1)[1], override_value)
                        for override_key, override_value in overr_params
                        if override_key.split('.', 1)[0] == match[0]
                    ]
                    combined_overrides = override_matches + specific_overrides
                    for override_match in combined_overrides:
                        if isinstance(override_match, tuple) and len(override_match) == 2:
                            override_key = override_match[0].strip()
                            override_value = override_match[1].strip()
                            Utils.update(inertial, f"inertials.{override_key}", override_value)
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
