import re
from lxml import etree
from dataclasses import is_dataclass, fields
from calibrator import Calibrator as calibrator
from eln import Electronics as electronics
from mec import Mechanicals as mechanical 
from motorControl import motorControl
from mc_service import Service as service

class Part:
    def __init__(self):
        self.calibration = list[calibrator]
        self.eln = list[electronics]
        self.mechanicals = list[mechanical]
        self.motorcontrol = list[motorControl]
        self.service = list[service]

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/partsTree.sysml', 'r') as file:
            sysml_str = file.read()

        part = cls()
        part_pattern = r'part\s+(\w+)\s+\[(\d+)\]\s+:\>\s+(\w+)'
        part_matches = re.findall(part_pattern, sysml_str)

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
            else:
                print("No match found")

        return part

    def to_xml(self, root_path):
        with open(root_path+'/partsTree.sysml', 'r') as file:
            sysml_str = file.read()

        subset_pattern = r'part \w+ subsets (\w+) = "([^"]+)"'
        for match in re.findall(subset_pattern, sysml_str):
            if match[0] == 'calibrator':
                for calibrator in self.calibration:
                    calibrator.to_xml(root_path, match[1])
            elif match[0] == 'eln':
                for electronics in self.eln:
                    electronics.to_xml(root_path, match[1])
            elif match[0] == 'mechanical':
                for mechanical in self.mechanicals:
                    mechanical.to_xml(root_path, match[1])
            elif match[0] == 'motorcontrol':
                for motorControl in self.motorcontrol:
                    motorControl.to_xml(root_path, match[1])
            elif match[0] == 'service':
                for service in self.service:
                    service.to_xml(root_path, match[1])
            else:
                print("No match found for part", match[0])

def main():
    part = Part.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    part.to_xml('/home/mgloria/iit/study-alexandria/sysml')

if __name__ == "__main__":
    main()
