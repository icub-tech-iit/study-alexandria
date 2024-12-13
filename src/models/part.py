import re
from lxml import etree
from calibrator import Calibrator as calibrator
from eln import Electronics as electronics
from mec import Mechanicals as mechanical 
from motorControl import motorControl
from mc_service import SERVICE

class Parts:
    def __init__(self):
        self.calibration = list[calibrator]
        self.eln = list[electronics]
        self.mechanicals = list[mechanical]
        self.motorcontrol = list[motorControl]
        self.service = list[SERVICE]

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
                part.service = [SERVICE.from_sysml(root_path) for i in range(0, int(match[1]))]
            else:
                print("No match found")

        return part

    @classmethod
    def to_xml(root_path):
        etree.indent(root_path, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root_path, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'/', "wb") as writer:
            writer.write(xml_object)

def main():
    part = Parts.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    print(part.__dict__)

if __name__ == "__main__":
    main()
