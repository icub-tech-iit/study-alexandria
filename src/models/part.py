import os
from utils import Utils
from calibrator import Calibrator as calibrator
from eln import Electronics as electronics
from mec import Mechanicals as mechanicals 
from motorControl import motorControl
from mc_service import Service as service
from inertial import Inertial as inertials
from pc104 import PC104 as pc104
from utils import Utils
class Part:
    def __init__(self):
        self.part_name = str
        self.calibrator = [calibrator]
        self.electronics = [electronics]
        self.mechanicals = [mechanicals]
        self.motorControl = [motorControl]
        self.service = [service]
        self.inertials = [inertials]
        self.pc104 = [pc104]

    @classmethod
    def from_sysml(cls, root_path, part):
        attr = dict(Utils.parse_sysml(root_path+'head.sysml').part_definitions.items())
        part = cls()
        parents = []

        for key, value in attr.items():
            if value.parent:
                if hasattr(part, value.parent):
                    parents.append(value.parent)

        for parent in parents:
            if hasattr(part, parent):
                subclass = getattr(part, parent)
                for item in subclass:
                    if hasattr(item, 'from_sysml'):
                        item = item.from_sysml(root_path)
                subclass.append(item)

        return part

    def to_xml(self, root_path, part, robot_name, overr_params):
        attr = dict(Utils.parse_sysml(root_path+'head_test.sysml').part_definitions.items())
        print(attr)
        Utils.check_subfolders_existance(root_path, robot_name)
        robot_path = os.path.join(root_path, robot_name)

        calibrators = self.calibrator[1:]
        electronics = self.electronics[1:]
        mechanicals = self.mechanicals[1:]
        motorControl = self.motorControl[1:]
        service = self.service[1:]
        inertials = self.inertials[1:]
        pc104 = self.pc104[1:]

        for cal in calibrators:
            print(cal)
            if hasattr(cal, 'to_xml'):
                cal.to_xml(robot_path, cal.name+".xml")


        # for match in re.findall(subset_pattern, sysml_str):
        #     override_matches = re.findall(override_pattern, match[3], re.DOTALL)
        #     if match[1] == 'calibrator':
        #         for calib in self.calibrator:
        #             specific_overrides = [
        #                 (override_key.split('.', 1)[1], override_value)
        #                 for override_key, override_value in overr_params
        #                 if override_key.split('.', 1)[0] == match[0]
        #             ]
        #             combined_overrides = override_matches + specific_overrides
        #             for override_match in combined_overrides:
        #                 if isinstance(override_match, tuple) and len(override_match) == 2:
        #                     override_key = override_match[0].strip()
        #                     override_value = override_match[1].strip()
        #                     Utils.update(calib, f"calibrator.{override_key}", override_value)
        #             calib.to_xml(robot_path, match[2])
            # elif match[1] == 'electronics':
            #     for electronic in self.eln:
            #         specific_overrides = [
            #             (override_key.split('.', 1)[1], override_value)
            #             for override_key, override_value in overr_params
            #             if override_key.split('.', 1)[0] == match[0]
            #         ]
            #         combined_overrides = override_matches + specific_overrides
            #         for override_match in combined_overrides:
            #             if isinstance(override_match, tuple) and len(override_match) == 2:
            #                 override_key = override_match[0].strip()
            #                 override_value = override_match[1].strip()
            #                 Utils.update(electronic, f"electronics.{override_key}", override_value)
            #         electronic.to_xml(robot_path, match[2])
            # elif match[1] == 'mechanical':
            #     for mech in self.mechanicals:
            #         specific_overrides = [
            #             (override_key.split('.', 1)[1], override_value)
            #             for override_key, override_value in overr_params
            #             if override_key.split('.', 1)[0] == match[0]
            #         ]
            #         combined_overrides = override_matches + specific_overrides
            #         for override_match in combined_overrides:
            #             if isinstance(override_match, tuple) and len(override_match) == 2:
            #                 override_key = override_match[0].strip()
            #                 override_value = override_match[1].strip()
            #                 Utils.update(mech, f"mechanicals.{override_key}", override_value)
            #         mech.to_xml(robot_path, match[2])
            # elif match[1] == 'motorControl':
            #     for motorControl in self.motorcontrol:
            #         specific_overrides = [
            #             (override_key.split('.', 1)[1], override_value)
            #             for override_key, override_value in overr_params
            #             if override_key.split('.', 1)[0] == match[0]
            #         ]
            #         combined_overrides = override_matches + specific_overrides
            #         for override_match in combined_overrides:
            #             if isinstance(override_match, tuple) and len(override_match) == 2:
            #                 override_key = override_match[0].strip()
            #                 override_value = override_match[1].strip()
            #                 Utils.update(motorControl, f"motorControl.{override_key}", override_value)
            #         motorControl.to_xml(robot_path, match[2])
            # elif match[1] == 'service':
            #     for service in self.service:
            #         specific_overrides = [
            #             (override_key.split('.', 1)[1], override_value)
            #             for override_key, override_value in overr_params
            #             if override_key.split('.', 1)[0] == match[0]
            #         ]
            #         combined_overrides = override_matches + specific_overrides
            #         for override_match in combined_overrides:
            #             if isinstance(override_match, tuple) and len(override_match) == 2:
            #                 override_key = override_match[0].strip()
            #                 override_value = override_match[1].strip()
            #                 Utils.update(service, f"SERVICE.{override_key}", override_value)
            #         service.to_xml(robot_path, match[2])
            # elif match[1] == 'inertials':
            #     for inertial in self.inertials:
            #         specific_overrides = [
            #             (override_key.split('.', 1)[1], override_value)
            #             for override_key, override_value in overr_params
            #             if override_key.split('.', 1)[0] == match[0]
            #         ]
            #         combined_overrides = override_matches + specific_overrides
            #         for override_match in combined_overrides:
            #             if isinstance(override_match, tuple) and len(override_match) == 2:
            #                 override_key = override_match[0].strip()
            #                 override_value = override_match[1].strip()
            #                 Utils.update(inertial, f"inertials.{override_key}", override_value)
            #         inertial.to_xml(robot_path, match[2])
            # elif match[1] == 'PC104':
            #     self.pc104.to_xml(robot_path, match[2])
            # else:
            #     print("No match found for part", match[1])

def main():
    part = Part.from_sysml('/home/mgloria/iit/study-alexandria/sysml/', 'head')
    # print(part.calibrator[0].from_sysml('/home/mgloria/iit/study-alexandria/sysml/').CALIB_ORDER)
    part.to_xml('/home/mgloria/iit/study-alexandria/sysml/', 'head', 'robot', {})
if __name__ == "__main__":
    main()
