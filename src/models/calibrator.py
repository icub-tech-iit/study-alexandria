import re
from lxml import etree
from dataclasses import dataclass
from phase import Phase
from device import Device

class Calibrator(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.CALIB_ORDER = list[float]
        self.phase = list[Phase]
    
    @dataclass
    class GENERAL:
        joints: int
        deviceName: str
    @dataclass
    class HOME:
        positionHome: list[float]
        velocityHome: list[float]

    @dataclass
    class CALIBRATION:
        calibrationType: list[float]
        calibration1: list[float]
        calibration2: list[float]
        calibration3: list[float]
        calibration4: list[float]
        calibration5: list[float]
        calibrationZero: list[float]
        calibrationDelta: list[float]

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/calibrator.sysml', 'r') as file:
            sysml_str = file.read()
    
        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            attributes = {}
            for match in matches:
                key = match[0]
                value = None
                if match[1]:
                    try:
                        value = float(match[1])
                    except ValueError:
                        value = match[1]
                elif match[2]:
                    value = int(match[2])
                else:
                    value = match[3]
                attributes[key] = value
            return attributes
        
        general_pattern = r'attribute (\w+) : \w+ default (?:(\d+(\.\d*)?)|"([^"]*)");' #catch integer/float with sign or quoted string
        vector_pattern = r'attribute (\w+) :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);'
        phase_pattern = r'attribute (\w+) : \w+ (\[\d+\]);'

        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern) | extract_attributes(sysml_str, phase_pattern)
        calib = cls(root_path)

        calib.general = cls.GENERAL(
            joints = attr['joints'],
            deviceName = calib.name
        )

        calib.home = cls.HOME(
            positionHome = [attr['positionHome']],
            velocityHome = [attr['velocityHome']]
        )

        calib.calibration = cls.CALIBRATION(
            calibrationType = [attr['calibrationType']],
            calibration1 = [attr['calibration1']],
            calibration2 = [attr['calibration2']],
            calibration3 = [attr['calibration3']],
            calibration4 = [attr['calibration4']],
            calibration5 = [attr['calibration5']],
            calibrationZero = [attr['calibrationZero']],
            calibrationDelta = [attr['calibrationDelta']],
        )

        calib.CALIB_ORDER = attr['CALIB_ORDER']
        calib.phase = [Phase.from_sysml(root_path) for i in attr['phase']]

        return calib

    def to_xml(root_path):
        with open(root_path+'/calibrator.sysml', 'r') as file:
            lines = file.readlines()
            
        def create_xml_node(parent, tag, attrib=None, text=None):
            element = etree.SubElement(parent, tag, attrib if attrib else {})
            if text:
                element.text = text
            return element
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': 'icub', 'build': '1'}, nsmap=nsmap)
        current_part, current_attribute = None, None
        stack, count = [], 0

        for line in lines:
            line = line.strip()
            element = line.split()[0]
            match element:
                case "import":
                    include_name = line.split()[1].strip('::*;')
                    if not include_name[0].istitle():
                        root.insert(0, etree.Element('{http://www.w3.org/2001/XInclude}include', {'href': f"{include_name}.xml"}))
                case "part":
                    c = count
                    while lines[c-1].startswith("attribute") or lines[c-1].strip().startswith("}"): # Fix indentation
                        stack.pop() if stack else None
                        c-=1
                    tokens = line.split()
                    name = tokens[1].strip(':')
                    datatype = None
                    attrib = {'name': name}
                    if datatype:
                        attrib['type'] = datatype
                    if '[' in line and ']' in line:  # Handle multiplicity
                        multiplicity = line[line.index('[') + 1:line.index(']')]
                        # current_part.set('multiplicity', multiplicity)
                    if ':' in tokens: # Verify if the part is a specification 
                        inher = tokens[3].strip(':')
                        if inher == 'device':
                        #     device_type = tokens[5].strip("=")
                            root = etree.Element('device', {'name': ' ', 'type': 'type'}, nsmap=nsmap)
                    else:
                        current_part = create_xml_node(stack[-1] if len(stack) > 0 else root, 'group', attrib)
                        stack.append(current_part)
                case "attribute":
                    c = count
                    while lines[c-1].startswith("attribute") or lines[c-1].strip().startswith("}"): # Fix indentation
                        stack.pop() if stack else None
                        c-=1
                    tokens = line.split()
                    name = tokens[1]
                    datatype = None
                    value = None
                    if '='  in line: # The attribute has a default value
                        value = tokens[5].strip(';') if len(tokens) > 5 else None
                    attrib = {'name': name}
                    if datatype:
                        attrib['type'] = datatype
                    current_attribute = create_xml_node(stack[-1] if len(stack) > 0 else root, 'param', attrib, value)
                    if '[' in line and ']' in line:  # Handle multiplicity
                        multiplicity = line[line.index('[') + 1:line.index(']')]
                        current_attribute.set('multiplicity', multiplicity)
            count += 1

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'calibrator.xml', "wb") as writer:
            writer.write(xml_object)

def main():
    root_path = "/home/mgloria/iit/study-alexandria/sysml/"
    # calibrator = Calibrator(root_path).from_sysml(root_path)
    Calibrator.to_xml(root_path)

if __name__ == "__main__":
    main()