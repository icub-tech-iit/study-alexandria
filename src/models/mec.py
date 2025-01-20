from dataclasses import dataclass, is_dataclass, fields
from lxml import etree
from utils import Utils
import re
class Mechanicals:
    @dataclass
    class GENERAL:
        MotioncontrolVersion: int
        Joints: int
        AxisMap: list[int]
        AxisName: list[str]
        AxisType: list[str]
        Encoder: list[float]
        fullscalePWM: list[int]
        ampsToSensor: list[float]
        Gearbox_M2J: list[float]
        Gearbox_E2J: list[int]
        useMotorSpeedFbk: list[int]
        MotorType: list[str]
        Verbose: int
    @dataclass
    class LIMITS:
        hardwareJntPosMin: list[int]
        hardwareJntPosMax: list[int]
        rotorPosMin: list[int]
        rotorPosMax: list[int]
    @dataclass
    class COUPLINGS:
        matrixJ2M: list[list[float]]
        matrixM2J: list[list[float]]
        matrixE2J: list[list[float]]
    @dataclass
    class JOINTSET_CFG:
        numberofsets: int
        @dataclass
        class JOINTSET_0:
            listofjoints: list[int]
            constraintName: str
            param1: int
            param2: int
        JOINTSET_0: JOINTSET_0

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/mec.sysml', 'r') as file:
            sysml_str = file.read()
    
        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            attributes = {}
            for match in matches:
                key = match[0]
                value = None
                if match[1]:
                    try:
                        value = float(match[1]) if isinstance(match[1], float) else int(match[1])
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

        mec = cls()
        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern)
        mec.GENERAL = cls.GENERAL(
            MotioncontrolVersion = attr['MotioncontrolVersion'],
            Joints = attr['Joints'],
            AxisMap = [item.strip() for item in attr['AxisMap'].split(",")],
            AxisName = [item.strip() for item in attr['AxisName'].split(",")],
            AxisType = [item.strip() for item in attr['AxisType'].split(",")],
            Encoder = [item.strip() for item in attr['Encoder'].split(",")],
            fullscalePWM = [item.strip() for item in attr['fullscalePWM'].split(",")],
            ampsToSensor = [item.strip() for item in attr['ampsToSensor'].split(",")],
            Gearbox_M2J = [item.strip() for item in attr['Gearbox_M2J'].split(",")],
            Gearbox_E2J = [item.strip() for item in attr['Gearbox_E2J'].split(",")],
            useMotorSpeedFbk = [item.strip() for item in attr['useMotorSpeedFbk'].split(",")],
            MotorType = [item.strip() for item in attr['MotorType'].split(",")],
            Verbose = attr['Verbose']
        )

        mec.LIMITS = cls.LIMITS(
            hardwareJntPosMin = [item.strip() for item in attr['hardwareJntPosMin'].split(",")],
            hardwareJntPosMax = [item.strip() for item in attr['hardwareJntPosMax'].split(",")],
            rotorPosMin = [item.strip() for item in attr['rotorPosMin'].split(",")],
            rotorPosMax = [item.strip() for item in attr['rotorPosMax'].split(",")],
        )

        mec.COUPLINGS = cls.COUPLINGS(
            matrixJ2M = [item.strip() for item in attr['matrixJ2M'].split(",")],
            matrixM2J = [item.strip() for item in attr['matrixM2J'].split(",")],
            matrixE2J = [item.strip() for item in attr['matrixE2J'].split(",")],
        )

        mec.JOINTSET_CFG = cls.JOINTSET_CFG(
            numberofsets = attr['numberofsets'],
            JOINTSET_0 = cls.JOINTSET_CFG.JOINTSET_0(
                listofjoints = [item.strip() for item in attr['listofjoints'].split(",")],
                constraintName = attr['constraintName'],
                param1 = attr['param1'],
                param2 = attr['param2']
            )
        )

        return mec
    
    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)
        
        Utils.check_subfolders_existance(root_path, file_name)
        
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
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    mec = Mechanicals.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    mec.to_xml('/home/mgloria/iit/study-alexandria/sysml', 'mec.xml')
    print(mec.JOINTSET_CFG.JOINTSET_0)

if __name__ == "__main__":
    main()