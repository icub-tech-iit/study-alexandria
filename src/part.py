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
from remapper import Remapper as remapper
from general import GENERAL as general
from xcub_all import Xcub_all as xcub_all
from utils import Utils
class Part:
    PART_CLASSES = {
        'calibrator': calibrator,
        'electronics': electronics,
        'mechanicals': mechanicals,
        'motorControl': motorControl,
        'service': service,
        'inertial': inertials,
        'PC104': pc104,
        'cartesian': cartesian,
        'ft': ft,
        'skin': skin,
        'skinSpec': skinSpec,
        'mais': mais,
        'dragonfly': dragonfly,
        'realsense': realsense,
        'wrapper': wrapper,
        'remapper': remapper,
        'GENERAL': general,
        'xcub_all': xcub_all        
    }

    def __init__(self):
        self.part_name = ""
        for attr in self.PART_CLASSES:
            setattr(self, attr, [])
    @classmethod
    def from_sysml(cls, root_path, part_name):
        attr = dict(Utils.parse_sysml(root_path+'/'+part_name+'.sysml').part_definitions.items())
        part = cls()
        parents = []

        for key, value in attr.items():
            if value.parent:
                if hasattr(part, value.parent):
                    parents.append(value.parent)
        return part

    def to_xml(self, root_path, part_name, robot_name, overr_params):
        attr = dict(Utils.parse_sysml(root_path+'/'+part_name+'.sysml').part_definitions.items())
        Utils.check_subfolders_existance(root_path, robot_name)
        robot_path = os.path.join(root_path, robot_name)

        for key, value in attr.items():
            if value.parent and value.parent in self.PART_CLASSES:
                part_class = self.PART_CLASSES[value.parent]
                if hasattr(part_class, 'from_sysml'):
                    instance = part_class.from_sysml(root_path)
                else:
                    instance = part_class()
                for specific_override_key, specific_override_value in Utils.extract_overrides(overr_params).items():
                    if key == specific_override_key:
                        value.parameters.update(specific_override_value)
                for override_key, override_value in value.parameters.items():
                    Utils.update(instance, f"{value.parent}.{override_key}", override_value)
                instance.to_xml(os.path.join(robot_path, Utils.extract_folder_name(instance)), f"{key}.xml")
            elif value.parent:
                print("No match found for part", value.parent)
        
def main():
    pass

if __name__ == "__main__":
    main()
