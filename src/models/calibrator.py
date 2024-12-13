import re
from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
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

    def to_xml(self, root_path):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': ' ', 'type': 'device_type'}, nsmap=nsmap)
        
        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.upper()})

            for field in fields(dataclass_instance):
                field_name = field.name
                field_value = getattr(dataclass_instance, field_name)
                
                if is_dataclass(field_value):
                    _dataclass_to_xml(group_elem, field_name, field_value) 
                elif isinstance(field_value, list):
                    if any(isinstance(i, list) for i in field_value):
                        param = etree.SubElement(group_elem, "param", {"name": field_name})
                        formatted_text = "\n".join(
                            "   ".join(map(str, row)) for row in field_value
                        )
                        param.text = f"\n{formatted_text}\n"
                    else:
                        param = etree.SubElement(group_elem, "param", {"name": field_name})
                        param.text = "   ".join(map(str, field_value))
                else:
                    param = etree.SubElement(group_elem, "param", {"name": field_name})
                    param.text = str(field_value)

        for attr_name, attr_value in self.__dict__.items():
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path + 'calibrator.xml', "wb") as writer:
            writer.write(xml_object)

def main():
    root_path = "/home/mgloria/iit/study-alexandria/sysml/"
    calibrator = Calibrator(root_path).from_sysml(root_path)
    calibrator.to_xml(root_path)

if __name__ == "__main__":
    main()