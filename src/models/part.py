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
        self.PC104 = [pc104]

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
        attr = dict(Utils.parse_sysml(root_path+'head.sysml').part_definitions.items())
        Utils.check_subfolders_existance(root_path, robot_name)
        robot_path = os.path.join(root_path, robot_name)

        calibrator = self.calibrator[1:]
        electronics = self.electronics[1:]
        mechanicals = self.mechanicals[1:]
        motorControl = self.motorControl[1:]
        service = self.service[1:]
        inertials = self.inertials[1:]
        pc104 = self.PC104[1:]

        for key, value in attr.items():
            if value.parent:
                match value.parent:
                    case 'calibrator':
                        for calib in calibrator:
                            for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                                if key == specific_override_key:
                                    value.parameters.update(specific_override_value)
                            for override_key, override_value in value.parameters.items():
                                Utils.update(calib, f"calibrator.{override_key}", override_value)
                            calib.to_xml(robot_path+'/calibrators/', key+'.xml')
                    case 'electronics':
                        for elec in electronics:
                            for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                                if key == specific_override_key:
                                    value.parameters.update(specific_override_value)
                            for override_key, override_value in value.parameters.items():
                                Utils.update(elec, f"electronics.{override_key}", override_value)
                            elec.to_xml(robot_path+'/hardware/electronics/', key+'.xml')
                    case 'mechanicals':
                        for mech in mechanicals:
                            for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                                if key == specific_override_key:
                                    value.parameters.update(specific_override_value)
                            for override_key, override_value in value.parameters.items():
                                Utils.update(mech, f"mechanicals.{override_key}", override_value)
                            mech.to_xml(robot_path+'/hardware/mechanicals/', key+'.xml')
                    case 'motorControl':
                        for motor in motorControl:
                            for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                                if key == specific_override_key:
                                    value.parameters.update(specific_override_value)
                            for override_key, override_value in value.parameters.items():
                                Utils.update(motor, f"motorControl.{override_key}", override_value)
                            motor.to_xml(robot_path+'/hardware/motorControl/', key+'.xml')
                    case 'service':
                        for serv in service:
                            for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                                if key == specific_override_key:
                                    value.parameters.update(specific_override_value)
                            for override_key, override_value in value.parameters.items():
                                Utils.update(serv, f"service.{override_key}", override_value)
                            serv.to_xml(robot_path+'/hardware/motorControl/', key+'.xml')
                    case 'inertials':
                        for inert in inertials:
                            for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                                if key == specific_override_key:
                                    value.parameters.update(specific_override_value)
                            for override_key, override_value in value.parameters.items():
                                Utils.update(inert, f"inertials.{override_key}", override_value)
                            inert.to_xml(robot_path+'/hardware/inertials/', key+'.xml')
                    case 'PC104':
                        for pc in pc104:
                            for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                                if key == specific_override_key:
                                    value.parameters.update(specific_override_value)
                            for override_key, override_value in value.parameters.items():
                                Utils.update(pc, f"pc104.{override_key}", override_value)
                            pc.to_xml(robot_path+'/hardware/electronics/', key+'.xml')
                    case _:
                        print("No match found for part", value.parent)

def main():
    part = Part.from_sysml('/home/mgloria/iit/study-alexandria/sysml/', 'head')
    part.to_xml('/home/mgloria/iit/study-alexandria/sysml/', 'head', 'robot', {})
if __name__ == "__main__":
    main()
