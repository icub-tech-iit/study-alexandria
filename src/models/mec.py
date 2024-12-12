from dataclasses import dataclass, is_dataclass, asdict, fields
from lxml import etree
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

        mec = cls()
        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern)
        mec.general = cls.GENERAL(
            MotioncontrolVersion = attr['MotioncontrolVersion'],
            Joints = attr['Joints'],
            AxisMap = [attr['AxisMap']],
            AxisName = [attr['AxisName']],
            AxisType = [attr['AxisType']],
            Encoder = [attr['Encoder']],
            fullscalePWM = [attr['fullscalePWM']],
            ampsToSensor = [attr['ampsToSensor']],
            Gearbox_M2J = [attr['Gearbox_M2J']],
            Gearbox_E2J = [attr['Gearbox_E2J']],
            useMotorSpeedFbk = [attr['useMotorSpeedFbk']],
            MotorType = [attr['MotorType']],
            Verbose = attr['Verbose']
        )

        mec.limits = cls.LIMITS(
            hardwareJntPosMin = [attr['hardwareJntPosMin']],
            hardwareJntPosMax = [attr['hardwareJntPosMax']],
            rotorPosMin = [attr['rotorPosMin']],
            rotorPosMax = [attr['rotorPosMax']]
        )

        mec.couplings = cls.COUPLINGS(
            matrixJ2M = [attr['matrixJ2M']],
            matrixM2J = [attr['matrixM2J']],
            matrixE2J = [attr['matrixE2J']]
        )

        mec.jointset_cfg = cls.JOINTSET_CFG(
            numberofsets = attr['numberofsets']
        )
        mec.jointset_0 = cls.JOINTSET_CFG(mec.jointset_cfg.numberofsets).JOINTSET_0(
            listofjoints = [attr['listofjoints']],
            constraintName = attr['constraintName'],
            param1 = attr['param1'],
            param2 = attr['param2']
        )

        return mec
    
    def to_xml(self, root_path):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)

        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.upper()})
            for field_name, field_value in asdict(dataclass_instance).items():
                if fields(dataclass_instance):
                    param = etree.SubElement(group_elem, "param", {"name": field_name})
                    param.text = " ".join(map(str, field_value)) if isinstance(field_value, list) else str(field_value)                    
                else:
                    _dataclass_to_xml(group_elem, field_name, field_value)
        for attr_name, attr_value in self.__dict__.items():
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        # Write to file
        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path + 'mec.xml', "wb") as writer:
            writer.write(xml_object)

def main():
    mec = Mechanicals.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    print(mec.jointset_0.constraintName)
    mec.to_xml('/home/mgloria/iit/study-alexandria/sysml/')

if __name__ == "__main__":
    main()