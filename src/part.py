import os
from utils import Utils
from calibrator import Calibrator as calibrator
from eln import Electronics as electronics
from mec import Mechanicals as mechanicals 
from motorControl import motorControl
from mc_service import Service as service
from inertial import Inertial as inertials
from pc104 import PC104 as pc104
from cartesian import Cartesian as cartesian
from ft import FT as ft
from skin import Skin as skin
from skinSpec import skinSpec
from mais import MAIS as mais
from dragonfly import Dragonfly as dragonfly
from realsense import Realsense as realsense
from wrapper import Wrapper as wrapper
from utils import Utils
class Part:
    def __init__(self):
        self.part_name = str
        self.calibrator = [calibrator]
        self.electronics = [electronics]
        self.mechanicals = [mechanicals]
        self.motorControl = [motorControl]
        self.service = [service]
        self.inertial = [inertials]
        self.PC104 = [pc104]
        self.cartesian = [cartesian]
        self.ft = [ft]
        self.skin = [skin]
        self.skinSpec = [skinSpec]
        self.mais = [mais]
        self.dragonfly = [dragonfly]
        self.realsense = [realsense]
        self.wrapper = [wrapper]

    @classmethod
    def from_sysml(cls, root_path, part_name):
        attr = dict(Utils.parse_sysml(root_path+'/'+part_name+'.sysml').part_definitions.items())
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

    def to_xml(self, root_path, part_name, robot_name, overr_params):
        attr = dict(Utils.parse_sysml(root_path+'/'+part_name+'.sysml').part_definitions.items())
        Utils.check_subfolders_existance(root_path, robot_name)
        robot_path = os.path.join(root_path, robot_name)

        calibrator = self.calibrator[1:]
        electronics = self.electronics[1:]
        mechanicals = self.mechanicals[1:]
        motorControl = self.motorControl[1:]
        service = self.service[1:]
        inertial = self.inertial[1:]
        pc104 = self.PC104[1:]
        cartesian = self.cartesian[1:]
        ft = self.ft[1:]
        skin = self.skin[1:]
        skinSpec = self.skinSpec[1:]
        mais = self.mais[1:]
        dragonfly = self.dragonfly[1:]
        realsense = self.realsense[1:]
        wrapper = self.wrapper[1:]

        for key, value in attr.items():
            if value.parent:
                def generate_xml(subclass, prefix, folder):
                    for item in subclass:                            
                        for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                            if key == specific_override_key:
                                value.parameters.update(specific_override_value)
                        for override_key, override_value in value.parameters.items():
                            Utils.update(item, f"{prefix}.{override_key}", override_value)
                        item.to_xml(os.path.join(robot_path, folder), f"{key}.xml")
 
                xml_map = {
                    'calibrator': (calibrator, 'calibrator', 'calibrators/'),
                    'electronics': (electronics, 'electronics', 'hardware/electronics/'),
                    'mechanicals': (mechanicals, 'mechanicals', 'hardware/mechanicals/'),
                    'motorControl': (motorControl, 'motorControl', 'hardware/motorControl/'),
                    'service': (service, 'service', 'hardware/motorControl/'),
                    'inertial': (inertial, 'inertials', 'hardware/inertials/'),
                    'ft': (ft, 'ft', 'hardware/FT/'),
                    'PC104': (pc104, 'pc104', 'hardware/electronics/'),
                    'cartesian': (cartesian, 'cartesian', 'cartesian/'),
                    'skin': (skin, 'skin', 'hardware/skin/'),
                    'skinSpec': (skinSpec, 'skinSpec', 'hardware/skin/'),
                    'mais': (mais, 'mais', 'hardware/MAIS/'),
                    'dragonfly': (dragonfly, 'dragonfly', 'camera/'),
                    'realsense': (realsense, 'realsense', 'camera/'),
                    'wrapper': (wrapper, 'wrapper', 'wrapper/motorControl/'),
                    # 'wrapper': (wrapper, 'wrapper', 'wrapper/FT/'),
                    # 'wrapper': (wrapper, 'wrapper', 'wrapper/inertials/'),
                }
 
                if value.parent in xml_map:
                    subclass, prefix, folder = xml_map[value.parent]
                    generate_xml(subclass, prefix, folder)
                else:
                    print("No match found for part", value.parent)
        
def main():
    pass

if __name__ == "__main__":
    main()
